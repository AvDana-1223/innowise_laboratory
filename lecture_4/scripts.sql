-- Create Table 1: students
CREATE TABLE IF NOT EXISTS students
(
    id         INTEGER Primary key,
    full_name  TEXT,
    birth_year INTEGER
);


-- Create Table 2: grades
CREATE TABLE IF NOT EXISTS grades
(
    id         INTEGER Primary key,
    student_id INTEGER,
    subject    TEXT,
    grade      INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id)
);


-- Adding data to Table 1: students
INSERT INTO students(full_name, birth_year) VALUES
    ('Alice Johnson', 2005),
    ('Brian Smith', 2004),
    ('Carla Reyes', 2006),
    ('Daniel Kim', 2005),
    ('Eva Thompson', 2003),
    ('Felix Nguyen', 2007),
    ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006);


-- Adding data to Table 2: grades
INSERT INTO grades(student_id, subject, grade) VALUES
    (1, 'Math', 88),
    (1, 'English', 92),
    (1, 'Science', 85),
    (2, 'Math', 75),
    (2, 'History', 83),
    (2, 'English', 79),
    (3, 'Science', 95),
    (3, 'Math', 91),
    (3, 'Art', 89),
    (4, 'Math', 84),
    (4, 'Science', 88),
    (4, 'Physical Education', 93),
    (5, 'English', 90),
    (5, 'History', 85),
    (5, 'Math', 88),
    (6, 'Science', 72),
    (6, 'Math', 78),
    (6, 'English', 81),
    (7, 'Art', 94),
    (7, 'Science', 87),
    (7, 'Math', 90),
    (8, 'History', 77),
    (8, 'Math', 83),
    (8, 'Science', 80),
    (9, 'English', 96),
    (9, 'Math', 89),
    (9, 'Art', 92);


-- Find all the grades of specific student (e.g. Alice Johnson)
SELECT g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.full_name = 'Alice Johnson';


-- Calculate the average grade of each student
SELECT s.id, s.full_name, avg(g.grade) AS avg_grade
FROM students s
LEFT JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY s.id;


-- The students who were born after 2004 were listed
SELECT s.id, s.full_name, s.birth_year
FROM students s
WHERE s.birth_year > 2004
ORDER BY s.birth_year, s.full_name;


-- Created a query that lists all the subjects and their average grades
SELECT g.subject, AVG(g.grade)
FROM grades g
GROUP BY g.subject;


-- Found three students with the highest average grades
SELECT s.full_name, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.full_name
ORDER BY avg_grade DESC
LIMIT 3;


-- Found all the students who scored less than 80 points in any subject
SELECT DISTINCT s.id, s.full_name
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80
ORDER BY s.id;

