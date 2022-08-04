-- Задание 1

SELECT count(*)
FROM tickets; -- 829071

SELECT count(*)
FROM tickets
WHERE passenger_name LIKE '% %'; -- 829071

SELECT count(*)
FROM tickets
WHERE passenger_name LIKE '% % %'; -- 0

SELECT count(*)
FROM tickets
WHERE passenger_name LIKE '% %%'; -- 829071

-- Задание 2

SELECT passenger_name
FROM tickets
WHERE passenger_name LIKE '___ %';

SELECT passenger_name
FROM tickets
WHERE passenger_name LIKE '% _____';

-- Задание 3
-- -- https://postgrespro.ru/docs/postgrespro/9.5/functions-matching#functions-similarto-regexp
-- -- regexp
SELECT passenger_name
FROM tickets
WHERE passenger_name SIMILAR TO '% (A|B)%' -- фамилия начинается с А или В
GROUP BY passenger_name;

