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

SELECT * FROM aircrafts_tmp;

-- Использование COPY для вывода в файлэ
COPY aircrafts_tmp TO '/work/backend-way/sql-way/postgreSQL_book/data/for_copy_out_chapter7.csv'
WITH (FORMAT csv);

