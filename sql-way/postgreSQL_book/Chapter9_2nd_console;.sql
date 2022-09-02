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
