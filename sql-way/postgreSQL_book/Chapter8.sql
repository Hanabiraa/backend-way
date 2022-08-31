-- Задание 2
CREATE TEMP TABLE tickets_tmp AS
SELECT *
FROM tickets WITH DATA;

ALTER TABLE tickets_tmp
    ADD PRIMARY KEY (ticket_no);

SELECT count(*)
FROM tickets_tmp
WHERE passenger_name = 'IVAN IVANOV';
-- 77 мс

-- Добавление индекса
CREATE INDEX passenger_name_idx ON tickets_tmp (passenger_name)
    WHERE passenger_name = 'IVAN IVANOV';

SELECT count(*)
FROM tickets_tmp
WHERE passenger_name = 'IVAN IVANOV';
-- 20 мс

-- Задание 3

SELECT count(*)
FROM ticket_flights
WHERE fare_conditions = 'Comfort'; -- 180 мс

SELECT count(*)
FROM ticket_flights
WHERE fare_conditions = 'Business'; -- 171 мс

SELECT count(*)
FROM ticket_flights
WHERE fare_conditions = 'Economy'; -- 222 мс

CREATE INDEX cond_idx ON ticket_flights (fare_conditions);

SELECT count(*)
FROM ticket_flights
WHERE fare_conditions = 'Comfort'; -- 25 мс

SELECT count(*)
FROM ticket_flights
WHERE fare_conditions = 'Business'; -- 60 мс

SELECT count(*)
FROM ticket_flights
WHERE fare_conditions = 'Economy';
-- 226 мс

-- -- Плохая селективность ведет к проблемам

-- Задание 4

CREATE INDEX complete_idx
    ON aircrafts_data (aircraft_code DESC NULLS FIRST, range ASC NULLS LAST);

\di+ complete_idx;



