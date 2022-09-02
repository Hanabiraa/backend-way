-- Стандартный уровень изоляции
SHOW default_transaction_isolation;

--  Проверка уровня изоляции READ COMMITTED
BEGIN;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SHOW default_transaction_isolation;

UPDATE aircrafts_tmp
SET range = range + 100
WHERE aircraft_code = 'SU9';

SELECT *
FROM aircrafts_tmp
WHERE aircraft_code = 'SU9';

COMMIT;

--  Проверка уровня изоляции REPEATABLE READ

BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;

INSERT INTO aircrafts_tmp
VALUES ('IL9', 'Илюшин ИЛ96', 9800);

UPDATE aircrafts_tmp
SET range = range + 100
WHERE aircraft_code = '320';

END;

--  Проверка уровня изоляции SERIALIZABLE
CREATE TABLE modes
(
    num  integer,
    mode text
);

INSERT INTO modes
VALUES (1, 'LOW'),
       (2, 'HIGH');

SELECT *
FROM modes;

BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;

UPDATE modes
SET mode = 'HIGH'
WHERE mode = 'LOW'
RETURNING *;

SELECT *
FROM modes;

COMMIT;

-- Пример использования транзакций

BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;

INSERT INTO bookings (book_ref, book_date, total_amount)
VALUES ('ABC123', bookings.now(), 0);

INSERT INTO tickets (ticket_no, book_ref, passenger_id, passenger_name)
VALUES ('9991234567890', 'ABC123', '1234 123456', 'IVAN PETROV'),
       ('9991234567891', 'ABC123', '4321 654321', 'PETR IVANOV');

INSERT INTO ticket_flights (ticket_no, flight_id, fare_conditions, amount)
VALUES ('9991234567890', 5572, 'Business', 12500),
       ('9991234567890', 13881, 'Economy', 8500),
       ('9991234567891', 5572, 'Economy', 12500),
       ('9991234567891', 13881, 'Economy', 8500);

UPDATE bookings
SET total_amount = (SELECT sum(amount)
                    FROM ticket_flights
                    WHERE ticket_no IN (SELECT ticket_no
                                        FROM tickets
                                        WHERE book_ref = 'ABC123'))
WHERE book_ref = 'ABC123';

SELECT *
FROM bookings
WHERE book_ref = 'ABC123';

COMMIT;

-- Пример использования блокировок на уровне строк с целью их обновления
BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;

SELECT * FROM aircrafts_tmp
WHERE model ~ '^Аэр'
FOR UPDATE;

UPDATE aircrafts_tmp
SET range = 5800
WHERE aircraft_code = '320';

COMMIT;

-- пример блокировки на уровне таблиц
BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;

LOCK TABLE aircrafts_tmp
IN ACCESS EXCLUSIVE MODE;

ROLLBACK;

