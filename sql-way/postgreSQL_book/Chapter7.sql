-- создание временной таблицы (хранятся до отключения из базы данных) без данных
CREATE TEMP TABLE aircrafts_tmp AS
SELECT *
FROM aircrafts WITH NO DATA;

-- наложение ограничений на временную таблицу
ALTER TABLE aircrafts_tmp
    ADD PRIMARY KEY (aircraft_code),
    ADD UNIQUE (model);

-- создание второй временной таблицы для журналирования операций с первой
CREATE TEMP TABLE aircrafts_log AS
SELECT *
FROM aircrafts WITH NO DATA;

-- Добавление двух доп столбцов для логгирования
ALTER TABLE aircrafts_log
    ADD COLUMN when_add  timestamp,
    ADD COLUMN operation text;

-- Реализация логгирования при помощи общего табличного выражения (лучше использовать
-- триггеры или же правила)
WITH add_row AS
         (INSERT INTO aircrafts_tmp
             SELECT * FROM aircrafts
             RETURNING *)
INSERT
INTO aircrafts_log
SELECT add_row.aircraft_code,
       add_row.model,
       add_row.range,
       current_timestamp,
       'INSERT'
FROM add_row;

SELECT *
FROM aircrafts_tmp
ORDER BY model;

SELECT *
FROM aircrafts_log
ORDER BY model;

-- Создание конфликта по первичным ключам при добавлении новых строк
-- без разрешения конфликта (ON CONFLICT DO NOTHING)
-- -- Все будет выполнено без сообщений об ошибках, но строка доавблена не будет
WITH add_row AS
         (INSERT INTO aircrafts_tmp
             VALUES ('SU9', 'Сухой Суперджет-100', 3000)
             ON CONFLICT DO NOTHING
             RETURNING *)
INSERT
INTO aircrafts_log
SELECT add_row.aircraft_code,
       add_row.model,
       add_row.range,
       current_timestamp,
       'INSERT'
FROM add_row;

-- Указание какой именно столбец проверять на конфликтующие значения
INSERT INTO aircrafts_tmp
VALUES ('SU9', 'Сухой Суперджет-100', 3000)
ON CONFLICT (aircraft_code) DO NOTHING
RETURNING *;

-- Обход ограничения на конфликт по столбцу aircraft_code, но далее идет проверка на уникальность
-- стобца model и вызывается ошибка из-за несоответствия по уникальности
INSERT INTO aircrafts_tmp
VALUES ('S99', 'Сухой Суперджет-100', 3000)
ON CONFLICT (aircraft_code) DO NOTHING
RETURNING *;

-- при конфликте по уникальному ключу - обновлять запись, а именно поля model и range
INSERT INTO aircrafts_tmp
VALUES ('SU9', 'Сухой Суперджет', 3000)
ON CONFLICT ON CONSTRAINT aircrafts_tmp_pkey
    DO UPDATE SET model = excluded.model,
                  range = excluded.range
RETURNING *;

-- Применение комманды COPY к файлу формата csv
COPY aircrafts_tmp FROM '/work/backend-way/sql-way/postgreSQL_book/data/for_copy_chapter7.csv'
    WITH (FORMAT csv);

SELECT *
FROM aircrafts_tmp;

-- Использование COPY для вывода в файл
COPY aircrafts_tmp TO '/work/backend-way/sql-way/postgreSQL_book/data/for_copy_out_chapter7.csv'
    WITH (FORMAT csv);

-- Использование команды UPDATE с логгированием
WITH update_row AS
         (UPDATE aircrafts_tmp
             SET range = range * 1.2
             WHERE model ~ '^Бом'
             RETURNING *)
INSERT
INTO aircrafts_log
SELECT ur.aircraft_code, ur.model, ur.range, current_timestamp, 'UPDATE'
FROM update_row AS ur;

SELECT *
FROM aircrafts_log
ORDER BY when_add DESC;

-- Реализация задачи: динамика продаж билетов по всем направлениям и датой последнего увеличения их числа
CREATE TEMP TABLE tickets_directions AS
SELECT DISTINCT departure_city, arrival_city
FROM routes;

ALTER TABLE tickets_directions
    ADD COLUMN last_ticket_time timestamp,
    ADD COLUMN tickets_num      integer DEFAULT 0;

-- -- Создание временной таблицы "Перелеты" без внешних ключей для упрощения
CREATE TEMP TABLE ticket_flights_tmp AS
SELECT *
FROM ticket_flights WITH NO DATA;

ALTER TABLE ticket_flights_tmp
    ADD PRIMARY KEY (ticket_no, flight_id);

-- -- Сама команда добавления новой записи о продаже билетоа и увеличения количества билетом по текущему направлению билета
WITH sell_ticket AS
         (INSERT INTO ticket_flights_tmp (ticket_no, flight_id, fare_conditions, amount)
             VALUES ('1234567890123', 30829, 'Economy', 12800)
             RETURNING *)
UPDATE tickets_directions AS td
SET last_ticket_time = current_timestamp,
    tickets_num      = tickets_num + 1
WHERE (td.departure_city, td.arrival_city) =
      (SELECT departure_city, arrival_city
       FROM flights_v
       WHERE flight_id = (SELECT flight_id
                          FROM sell_ticket));

-- -- Проверка добавления
SELECT *
FROM tickets_directions
WHERE last_ticket_time IS NOT NULL;

-- -- Тот же самый запрос, но посредством объединения таблиц
WITH sell_ticket AS
         (INSERT INTO ticket_flights_tmp (ticket_no, flight_id, fare_conditions, amount)
             VALUES ('1234567890123', 7757, 'Economy', 3400)
             RETURNING *)
UPDATE tickets_directions AS td
SET last_ticket_time = current_timestamp,
    tickets_num      = tickets_num + 1
FROM flights_v AS f
WHERE td.departure_city = f.departure_city
  AND td.arrival_city = f.arrival_city
  AND f.flight_id = (SELECT flight_id FROM sell_ticket);

-- применение комманды DELETE с логгированием

WITH delete_row AS
         (DELETE FROM aircrafts_tmp
             WHERE model ~ '^Бом'
             RETURNING *)
INSERT
INTO aircrafts_log
SELECT dr.aircraft_code,
       dr.model,
       dr.range,
       current_timestamp,
       'DELETE'
FROM delete_row AS dr;

SELECT *
FROM aircrafts_log
ORDER BY when_add DESC;

-- Удаление строк при помощи USING и WHERE
WITH min_ranges AS
         (SELECT aircraft_code,
                 rank() OVER (
                     PARTITION BY left(model, 6)
                     ORDER BY range
                     ) AS rank
          FROM aircrafts_tmp
          WHERE model ~ '^Аэробус'
             OR model ~ '^Боинг')
DELETE
FROM aircrafts_tmp AS a
    USING min_ranges AS mr
WHERE a.aircraft_code = mr.aircraft_code
  AND mr.rank = 1
RETURNING *;

-- Задание 1
SELECT *
FROM aircrafts_log;

ALTER TABLE aircrafts_log
    ALTER COLUMN when_add SET DEFAULT current_timestamp;

-- -- Проверка
INSERT
INTO aircrafts_log (aircraft_code, model, range, operation)
VALUES ('675', 'Боинг 675-300', 5432, 'INSERT');

SELECT *
FROM aircrafts_log
ORDER BY when_add DESC;

-- Задание 2
WITH add_row AS
         (INSERT INTO aircrafts_tmp
             SELECT * FROM aircrafts
             ON CONFLICT DO NOTHING
             RETURNING aircraft_code, model, range, current_timestamp, 'INSERT')
INSERT
INTO aircrafts_log
SELECT *
FROM add_row;

-- Задание 3
DELETE
FROM aircrafts_tmp
WHERE TRUE;

INSERT INTO aircrafts_tmp
SELECT *
FROM aircrafts
RETURNING *;

-- Задание 4
CREATE TEMP TABLE seats_tmp AS
SELECT *
FROM seats;

ALTER TABLE seats_tmp
    ADD PRIMARY KEY (aircraft_code, seat_no);

SELECT *
FROM seats_tmp;

-- -- Проверка на дублирование с использованием перечисления столбцов
INSERT INTO seats_tmp
SELECT *
FROM seats
ON CONFLICT (aircraft_code, seat_no) DO NOTHING;

-- -- То же самое, но с ON CONSTRAINT
INSERT INTO seats_tmp
SELECT *
FROM seats
ON CONFLICT ON CONSTRAINT seats_tmp_pkey DO NOTHING;

-- Задание 5
WITH mod_row AS
         (INSERT INTO aircrafts_tmp
             SELECT *
             FROM aircrafts
             ON CONFLICT (aircraft_code) DO UPDATE
                 SET range = 12560
                 WHERE aircrafts_tmp.range < 499
             RETURNING aircraft_code, model, range, 'INSERT')
INSERT
INTO aircrafts_log (aircraft_code, model, range, operation)
SELECT *
FROM mod_row;

SELECT *
FROM aircrafts_tmp;

SELECT * FROM aircrafts_log;
