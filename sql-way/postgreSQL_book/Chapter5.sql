-- Глава 6.

-- -- Просмотр схемы по умолчанию
SHOW search_path;

-- Задание 1
CREATE TABLE students
(
    record_book  numeric(5) NOT NULL,
    name         text       NOT NULL,
    doc_ser      numeric(4),
    doc_num      numeric(6),
    who_adds_row text DEFAULT current_user,
    time_to_add  time DEFAULT current_time,
    PRIMARY KEY (record_book)
);

INSERT INTO students
VALUES (12300, 'Иванов Иван Васильевич', 0402, 543281);

SELECT *
FROM students;

-- -- Смена типа колонки с времени на время с датой
ALTER TABLE students
    DROP COLUMN time_to_add,
    ADD COLUMN date_to_add timestamptz,
    ALTER COLUMN date_to_add SET DEFAULT now();

INSERT INTO students
VALUES (99900, 'Петров Петр Петрович', 1387, 127001);

-- -- Заполнение null столбцов значениями по default
UPDATE students
SET date_to_add = DEFAULT
WHERE date_to_add IS NULL;


SELECT *
FROM students;

-- Задание 2

CREATE TABLE progress
(
    record_book numeric(5) NOT NULL,
    subject     text       NOT NULL,
    acad_year   text       NOT NULL,
    term        numeric(1) NOT NULL
        CHECK (term = 1 or term = 2),
    mark        numeric(1) NOT NULL
        CHECK (mark >= 3 or mark <= 5)
        DEFAULT 5,
    FOREIGN KEY (record_book) REFERENCES students (record_book)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- -- Добавление колонки с ограничением и удалением предыдущего ограничения
ALTER TABLE progress
    ADD COLUMN test_form text,
    ADD CONSTRAINT check_mark_for_test_form CHECK
        (
            (test_form = 'экзамен' AND mark IN (3, 4, 5))
            OR
            (test_form = 'зачет' AND mark IN (0, 1))
        ),
    DROP CONSTRAINT progress_term_check1;

INSERT INTO progress
VALUES (99900, 'math', '1', 1, 1, 'зачет'),
       (99900, 'math', '1', 1, 4, 'экзамен'),
       (99900, 'biology', '2', 2, 0, 'зачет'),
       (99900, 'biology', '2', 2, 5, 'экзамен'),
       (12300, 'math', '3', 2, 3, 'экзамен'),
       (12300, 'math', '3', 2, 4, 'экзамен'),
       (12300, 'physics', '1', 1, 0, 'зачет'),
       (12300, 'physics', '2', 2, 1, 'зачет');

SELECT *
FROM progress;

-- -- Вызов ошибки при вставке
INSERT INTO progress
VALUES (99900, 'math', '1', 1, 8, 'зачет'),
       (99900, 'math', '1', 1, 2, 'что-то');

-- Задание 3

ALTER TABLE progress
    ALTER COLUMN term DROP NOT NULL,
    ALTER COLUMN mark DROP NOT NULL;

-- -- Проверка, хватит ли ограничений без ограничения not null
INSERT INTO progress
VALUES (99900, 'chemistry', '6', 1, NULL, 'зачет'),
       (99900, 'chemistry', '6', 1, NULL, 'экзамен');

SELECT *
FROM progress;

SELECT NOT NULL > 5;

-- -- Вывод - ограничение not null должно быть наложено, даже когда есть ограничения помимо

DELETE
FROM progress
WHERE mark IS NULL;

ALTER TABLE progress
    ALTER COLUMN term SET NOT NULL,
    ALTER COLUMN mark SET NOT NULL;

-- Задание 5
ALTER TABLE students
    ADD UNIQUE (doc_ser),
    ADD UNIQUE (doc_num);

INSERT INTO students
VALUES (40601, 'Григорьев Михаил Иванович', 0107, NULL),
       (32500, 'Михайлов Альберт Давидович', NULL, NULL);

SELECT *
FROM students;

-- Задание 6

DROP TABLE progress, students;

CREATE TABLE students
(
    record_book numeric(5) NOT NULL UNIQUE,
    name        text       NOT NULL,
    doc_ser     numeric(4),
    doc_num     numeric(6),
    PRIMARY KEY (doc_ser, doc_num)
);

CREATE TABLE progress
(
    doc_ser   numeric(4),
    doc_num   numeric(6),
    subject   text       NOT NULL,
    acad_year text       NOT NULL,
    term      numeric(1) NOT NULL
        CHECK (term IN (1, 2)),
    mark      numeric(1) NOT NULL
        CHECK (mark >= 3 AND mark <= 5)
        DEFAULT 5,
    FOREIGN KEY (doc_ser, doc_num)
        REFERENCES students
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO students
VALUES (40601, 'Григорьев Михаил Иванович', 0107, 101201),
       (32500, 'Михайлов Альберт Давидович', 0108, 321321),
       (34120, 'Михайлов Альберт Давидович', 0109, 321321),
       (61503, 'Михайлов Альберт Давидович', 0110, 127901),
       (75931, 'Михайлов Альберт Давидович', 0111, 909090);

SELECT *
FROM students;

INSERT INTO progress
VALUES (0107, 101201, 'math', 'start', 1, 3),
       (0108, 321321, 'math', 'end', 2, 3),
       (0108, 321321, 'biology', 'start', 1, 5),
       (0107, 101201, 'biology', 'end', 2, 4),
       (0109, 321321, 'math', 'start', 1, 3),
       (0110, 127901, 'math', 'end', 2, 3),
       (0111, 909090, 'physics', 'end', 1, 5),
       (0110, 127901, 'physics', 'start', 2, 4);

SELECT *
FROM progress
ORDER BY doc_ser, doc_num DESC;


-- Задание 8

CREATE TABLE subjects
(
    subject_id integer,
    subject    text UNIQUE,
    PRIMARY KEY (subject_id)
);

INSERT INTO subjects
VALUES (1, 'math'),
       (2, 'biology'),
       (3, 'physics'),
       (4, 'chemistry');

SELECT *
FROM subjects;

-- -- изменение колонки "предметы", добавление внешнего ключа
ALTER TABLE progress
    RENAME COLUMN subject TO subject_id;

ALTER TABLE progress
    ALTER COLUMN subject_id TYPE integer
        USING (CASE
                   WHEN progress.subject_id = 'math' THEN 1
                   WHEN progress.subject_id = 'biology' THEN 2
                   WHEN progress.subject_id = 'physics' THEN 3
                   ELSE 4 END),
    ADD FOREIGN KEY (subject_id) REFERENCES subjects (subject_id);

INSERT INTO progress
VALUES (110, 127901, 4, 'start', 1, 5),
       (111, 909090, 4, 'start', 1, 5),
       (109, 321321, 4, 'start', 1, 5),
       (107, 101201, 4, 'start', 1, 5);

SELECT *
FROM progress;

-- Задание 9

ALTER TABLE students
    ADD CONSTRAINT check_name CHECK (name <> '');

-- модификация для недопускания пробельных символов
ALTER TABLE students
    DROP CONSTRAINT check_name,
    ADD CONSTRAINT check_name CHECK ( trim(both from name) <> '');

-- Задание 10

-- -- смена типа основного ключа c integer на text

-- -- -- Для начала удаляем foreign key в ссылающейся таблице
-- -- -- и меняем тип столбца в ней
ALTER TABLE progress
    DROP CONSTRAINT progress_doc_ser_doc_num_fkey,
    ALTER COLUMN doc_ser TYPE text USING cast(doc_ser AS text);

-- -- -- Меняем тип primary key в ссылочной таблице
ALTER TABLE students
    ALTER COLUMN doc_ser TYPE text USING cast(doc_ser AS text);

-- -- -- Снова привязываем foreign key в ссылающейся таблице
ALTER TABLE progress
    ADD FOREIGN KEY (doc_ser, doc_num) REFERENCES students (doc_ser, doc_num)

-- -- -- проверка
INSERT INTO students
VALUES (55532, 'Кристофер Нолан Андреевич', '0409', 512000);

INSERT INTO progress
VALUES ('0409', 512000, 3, 'end', 1, 5);

SELECT *
FROM progress;

SELECT *
FROM students;

-- Задание 17

-- -- вертикальное view (т.е. часть столбцов)
CREATE VIEW airports_names AS
    SELECT airport_code, airport_name, city
    FROM demo.bookings.airports;

-- -- горизонтальное view (т.е. часть строк)
CREATE VIEW siberian_airports AS
    SELECT * FROM airports
    WHERE city = 'Новосибирск' OR city = 'Кемерово';

-- -- пример и вертикального и горизонтального view (не все столбцы и не все строки)
CREATE OR REPLACE VIEW airports_names AS
    SELECT airport_code, airport_name, city
    FROM demo.bookings.airports
    WHERE airport_name <> city;
