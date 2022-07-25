-- Глава: ОСНОВНЫЕ ТИПЫ ДАННЫХ
-- Задание 12
SHOW datestyle;

SELECT '18 may 2016'::date, '18 may 2016'::timestamp;
SELECT '18-05-2016'::date, '2016-05-18'::timestamp;

SET datestyle TO 'MDY';
SELECT '18 may 2016'::date, '18 may 2016'::timestamp;
SELECT '05-18-2016'::date, '05-18-2016'::timestamp;

SET datestyle TO 'ISO, DMY';
SHOW datestyle;

-- Задание 15
SELECT to_char(current_timestamp, 'mi:ss');
SELECT to_char(current_timestamp, 'hh24:mi:ss');
SELECT to_char(current_timestamp, 'dd');
SELECT to_char(current_timestamp, 'yyyy-mm-dd');
SELECT to_char(current_timestamp, 'yyyy-mm, TZ OF');

-- Задание 16
-- вызов ошибки
SELECT '21-21-2021'::date;

-- Задание 17
-- вызов ошибки
SELECT '21:15:16:22'::time;

-- Задание 18
SELECT ('2016-09-16'::date - '2016-09-01'::date); -- тип значения - integer

-- Задание 19
SELECT ('20:34:35'::time - '19:44:45'::time); -- тип значения - interval
SELECT ('20:34:35'::time + '19:44:45'::time); -- ошибка, такой операции для типа данных time + time нет

-- Задание 20
SELECT (current_timestamp - '2020-01-01'::timestamp) AS new_date;   -- тип результата interval,
                                                                    -- но только с днями (даже если их больше 365) без
                                                                    -- перевода в года и месяцы

SELECT age(current_timestamp, '2020-01-01'::timestamp) AS new_date; -- тип результата interval, но
                                                                    -- уже с учетом лет и месяцев

SELECT (current_timestamp + '1 mon'::interval) AS new_date;

-- Задание 23
