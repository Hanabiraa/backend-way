--  Проверка уровня изоляции READ COMMITTED
BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- -- Ожидание будет идти до тех пор, пока транзакция на первой консоли
-- -- либо не завершится комитом, либо ролбэком, т.к. строка заблокирована
UPDATE aircrafts_tmp
    SET range = range + 200
    WHERE aircraft_code = 'SU9';

SELECT * FROM aircrafts_tmp
    WHERE aircraft_code = 'SU9';

END; -- эквивалент COMMIT в postgre

--  Проверка уровня изоляции REPEATABLE READ

SELECT * FROM aircrafts_tmp;

-- -- данные изменились лишь после коммита транзакции с первой консоли,
-- -- до этого момента всегда выводились данные снапшота
SELECT * FROM aircrafts_tmp;

--  Проверка уровня изоляции SERIALIZABLE

BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;

UPDATE modes
    SET mode = 'LOW'
    WHERE mode = 'HIGH'
    RETURNING *;

SELECT * FROM modes;

-- -- Ошибка, ибо есть зависимость чтения/записи
-- -- обновление таблицы сделала та транзакция, которая была первой зафиксирована
-- -- а вторая транзакция завершилась с ошибкой
COMMIT;

-- Пример использования блокировок на уровне строк с целью их обновления
BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- -- не будет вызввана комманда, пока не завершится блокировка в транзакции на 1 консоле,
-- -- или иначе будет проблема неповторяющихся данных

SELECT * FROM aircrafts_tmp
WHERE model ~ '^Аэр'
FOR UPDATE;

UPDATE aircrafts_tmp
SET range = 5800
WHERE aircraft_code = '320';

COMMIT;

-- пример блокировки на уровне таблиц
BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- -- не будет выполнена, т.к. заблокирована вся таблица и необходимо ждать
-- -- снятия блокировки
SELECT * FROM aircrafts_tmp;

-- Задание 2
BEGIN;

SELECT  * FROM aircrafts_tmp
WHERE range < 2000;

-- -- у команды идет ожидание, когда на строки, подлежащие удалению,
-- -- будет снята блокировка, т.к. блокировка установленна командой
-- -- UPDATE
DELETE FROM aircrafts_tmp
WHERE range < 2000;

-- -- DELETE удалил 0 строчек, когда должен был одну, почему?
-- -- потому что блокировка со строки, которую обновили была снята
-- -- и команда ее перечитывает, ввиду того, что после обновления
-- -- она не попадает под удаление - ее игнорирует, но существует другая
-- -- строка, которая теперь попадает под удаление, но блок WHERE после
-- -- снятия блокировки не перечитывает все строки

END;

-- -- подзадание
BEGIN;

SELECT  * FROM aircrafts_tmp
WHERE range < 2000;

-- -- Будет удалена та строка, которая удовлетворяла условию до первой транзакции
-- -- т.к. первая транзакция была откатана
DELETE FROM aircrafts_tmp
WHERE range < 2000;

SELECT  * FROM aircrafts_tmp
WHERE aircraft_code = 'CR2' OR aircraft_code = 'CN1';

ROLLBACK;

-- Задание 6

BEGIN;

-- -- блокировка FOR SHARE не допускает операции
-- -- UPDATE, DELETE, SELECT FOR UPDATE или
-- -- SELECT FOR NO KEY UPDATE, но допускает
-- -- SELECT FOR SHARE и SELECT FOR KEY SHARE.
UPDATE aircrafts_tmp
    SET range = range * 0.2
WHERE range > 4000;

ROLLBACK;

-- Задание 9

BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;

UPDATE modes
    SET mode = 'LOW1'
    WHERE num = 100001;

COMMIT;

-- Задание 10

BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;

SELECT * FROM ticket_flights
WHERE flight_id = 5572;

INSERT INTO bookings (book_ref, book_date, total_amount)
VALUES ('ABC456', bookings.now(), 0);

INSERT INTO tickets (ticket_no, book_ref, passenger_id, passenger_name)
VALUES ('9991234567891', 'ABC456', '4321 654321', 'PETR IVANOV');

INSERT INTO ticket_flights (ticket_no, flight_id, fare_conditions, amount)
VALUES ('9991234567891', 5572, 'Business', 12500);

UPDATE bookings
    SET total_amount = 12500
    WHERE book_ref = 'ABC456';

COMMIT;