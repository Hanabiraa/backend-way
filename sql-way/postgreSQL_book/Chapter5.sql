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
SELECT ('2016-09-16'::date - '2016-09-01'::date);
-- тип значения - integer

-- Задание 19
SELECT ('20:34:35'::time - '19:44:45'::time); -- тип значения - interval
SELECT ('20:34:35'::time + '19:44:45'::time);
-- ошибка, такой операции для типа данных time + time нет

-- Задание 20
SELECT (current_timestamp - '2020-01-01'::timestamp) AS new_date;
-- тип результата interval,
-- но только с днями (даже если их больше 365) без
-- перевода в года и месяцы

SELECT age(current_timestamp, '2020-01-01'::timestamp) AS new_date;
-- тип результата interval, но
-- уже с учетом лет и месяцев

SELECT (current_timestamp + '1 mon'::interval) AS new_date;

-- Задание 23
SELECT ('2016-09-16'::date - '2016-09-11'::date) AS new_int_val;
SELECT ('2016-09-16'::timestamp - '2016-09-11'::timestamp) AS new_interval_val;

-- Задание 24
SELECT ('20:34:35'::time - 1); -- ошибка, нельзя вычитать из типа time тип integer
SELECT ('20:34:35'::time - '1'::interval) AS mod; -- можно модифицировать в интервал

SELECT ('2016-09-16'::date - 1) AS new_date;

-- Задание 25

SELECT date_trunc('microseconds', '1999-11-27 12:34:56.987654'::timestamp) AS microsec,
       date_trunc('milliseconds', '1999-11-27 12:34:56.987654'::timestamp) AS milisec,
       date_trunc('second', '1999-11-27 12:34:56.987654'::timestamp)       AS sec,
       date_trunc('minute', '1999-11-27 12:34:56.987654'::timestamp)       AS min,
       date_trunc('hour', '1999-11-27 12:34:56.987654'::timestamp)         AS hour,
       date_trunc('day', '1999-11-27 12:34:56.987654'::timestamp)          AS day,
       date_trunc('week', '1999-11-27 12:34:56.987654'::timestamp)         AS week,
       date_trunc('month', '1999-11-27 12:34:56.987654'::timestamp)        AS month,
       date_trunc('quarter', '1999-11-27 12:34:56.987654'::timestamp)      AS quarter,
       date_trunc('year', '1999-11-27 12:34:56.987654'::timestamp)         AS year,
       date_trunc('decade', '1999-11-27 12:34:56.987654'::timestamp)       AS decade,
       date_trunc('century', '1999-11-27 12:34:56.987654'::timestamp)      AS century,
       date_trunc('millennium', '1999-11-27 12:34:56.987654'::timestamp)   AS millennium;

-- Задание 27
-- получение значение из типа timestamp, поля такие же, как и в date_trunc
SELECT extract('month' from '1999-10-01 12:34:56.987654'::timestamp) as month;

-- Задание 30
CREATE TABLE test_bool
(
    a boolean,
    b text
);

INSERT INTO test_bool
VALUES (TRUE, 'yes'),
       ('yes', true),
       (1::boolean, false),
       (false, '0'),
       ('f', '1'),
       ('t', '1');

SELECT *
FROM test_bool;

-- Задание 31
CREATE TABLE birthdays
(
    person   text NOT NULL,
    birthday date NOT NULL
);

INSERT INTO birthdays
VALUES ('Ken Thompson', '1955-03-23'),
       ('Ben Johnson', '1971-03-19'),
       ('Andy Gibson', '1987-08-12');

-- -- дни рождения в 3 месяце
SELECT *
from birthdays
WHERE extract('month' from birthday) = 3;

-- -- люди, достигшие возраста 40 лет
SELECT *
from birthdays
WHERE current_timestamp - birthday >= '40 years'::interval;


-- -- точный возраст человека на текущий момент
SELECT *,
       extract('year' from age(current_timestamp, birthday)) AS age
FROM birthdays;

-- Задание 32

-- -- Конкатенация массивов
SELECT array_cat(ARRAY [1, 2, 3], ARRAY [13, 5]); -- создание массивов по стандарту SQL
SELECT array_cat('{10000, 1, 100, 10}'::integer[], '{20, 3, 10000, 10000}'::integer[]);
-- синтаксис postgre

-- -- удаление элементов из массива (индексы начинаются с 1)
SELECT array_remove('{1, 2, 3, 4, 5}'::integer[], 2);

-- Задание 33
CREATE TABLE pilots
(
    pilot_name text,
    shedule    integer[],
    meal       text[]
);

INSERT INTO pilots
VALUES ('Ivan', '{1, 3, 5, 6, 7}', '{"Сосиска", "Макароны", "Кофе"}'),
       ('Petr', '{1, 2, 5, 7}', '{"Котлета", "Каша", "Кофе"}'),
       ('Pavel', '{1, 3, 5, 6, 7}', '{"Сосиска", "Каша", "Кофе"}'),
       ('Boris', '{1, 3, 5, 6, 7}', '{"Котлета", "Каша", "Чай"}');

SELECT *
FROM pilots;

-- -- выборка тех пилотов, в рационе которых есть определенный вид еды
SELECT *
FROM pilots
WHERE 'Сосиска' = any (meal);

DROP TABLE pilots;

-- -- двумерные массивы рационов
CREATE TABLE pilots
(
    pilot_name text,
    shedule    integer[],
    meal       text[][]
);

INSERT INTO pilots
VALUES ('Ivan', '{1, 3, 5, 6, 7}', '{
                                    {"Сосиска", "Макароны", "Кофе"},
                                    {"Котлета", "Каша", "Кофе"},
                                    {"Сосиска", "Каша", "Кофе"},
                                    {"Котлета", "Каша", "Чай"}
                                }'::text[][]),
       ('Petr', '{1, 2, 5, 7}', '{
                                    {"Сосиска", "Макароны", "Кофе"},
                                    {"Котлета", "Каша", "Кофе"},
                                    {"Сосиска", "Каша", "Кофе"},
                                    {"Котлета", "Каша", "Чай"}
                                }'::text[][]),
       ('Pavel', '{1, 3, 5, 6, 7}', '{
                                    {"Сосиска", "Макароны", "Кофе"},
                                    {"Котлета", "Каша", "Кофе"},
                                    {"Сосиска", "Каша", "Кофе"},
                                    {"Котлета", "Каша", "Чай"}
                                }'::text[][]),
       ('Boris', '{1, 3, 5, 6, 7}', '{
                                    {"Сосиска", "Макароны", "Кофе"},
                                    {"Котлета", "Каша", "Кофе"},
                                    {"Сосиска", "Каша", "Кофе"},
                                    {"Котлета", "Каша", "Чай"}
                                }'::text[][]);

SELECT *
FROM pilots;

UPDATE pilots
SET shedule = '{1, 2}'::integer[]
WHERE 3 = any (shedule);

SELECT *
FROM pilots;

-- Задание 34

CREATE TABLE pilots_hobbies
(
    pilot_name text,
    hobbies    jsonb
);

INSERT INTO pilots_hobbies
VALUES ('Ivan',
        '{
          "sports": [
            "футбол",
            "плавание"
          ],
          "home_lib": true,
          "trips": 3
        }'),
       ('Petr',
        '{
          "sports": [
            "теннис",
            "плавание"
          ],
          "home_lib": true,
          "trips": 2
        }'),
       ('Pavel',
        '{
          "sports": [
            "плавание"
          ],
          "home_lib": false,
          "trips": 4
        }'),
       ('Boris',
        '{
          "sports": [
            "футбол",
            "плавание",
            "теннис"
          ],
          "home_lib": true,
          "trips": 0
        }');

SELECT *
FROM pilots_hobbies;

UPDATE pilots_hobbies
SET hobbies = jsonb_set(hobbies, '{trips}', '10')
WHERE pilot_name = 'Pavel';

-- -- выборка тех пилотов, у которых есть домашняя библиотека и
-- -- количество поездок больше 1
SELECT pilot_name,
       hobbies -> 'trips'    AS trips,
       hobbies -> 'sports'   AS sports,
       hobbies -> 'home_lib' AS have_home_library
FROM pilots_hobbies
WHERE (hobbies -> 'home_lib')::bool = true
  AND (hobbies -> 'trips')::integer > 1;


SELECT *
FROM pilots_hobbies;

-- -- уменьшить количество поездок на 2 у тех пилотов, у которых нет домашней библиотеки
UPDATE pilots_hobbies
SET hobbies = jsonb_set(hobbies, '{trips}',
                        to_jsonb((hobbies -> 'trips')::integer - 2)
    )
WHERE (hobbies -> 'home_lib')::bool = false;

SELECT *
FROM pilots_hobbies
ORDER BY (hobbies -> 'home_lib')::bool DESC, (hobbies -> 'trips')::integer DESC;

-- Задание 35

-- -- конкатенация двух jsonb массивов
SELECT '{"sports": "хоккей"}'::jsonb || '{"trips": 5}'::jsonb;
