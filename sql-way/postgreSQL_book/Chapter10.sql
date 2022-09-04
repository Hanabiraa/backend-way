-- Задание 3
EXPLAIN
WITH CTE (book_ref, total_amount) AS
         (SELECT book_ref, total_amount
          FROM bookings
          WHERE total_amount > 50000)
SELECT book_ref, total_amount+10000 FROM CTE;

-- Задание 4
EXPLAIN
SELECT total_amount
FROM bookings
ORDER BY total_amount DESC
LIMIT 5;

-- Задание 5

EXPLAIN
SELECT city, count(*)
FROM airports
GROUP BY city
HAVING count(*) > 1;