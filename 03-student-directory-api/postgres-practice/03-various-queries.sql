-- find student with ID 5
SELECT * FROM students
WHERE student_id = 5;

-- change student 5's course to CS
UPDATE students
SET student_course = 'Bachelor of Science in Computer Science'
WHERE student_id = 5
RETURNING *;

-- delete student whose ID is 10
DELETE FROM students
WHERE student_id = 10
RETURNING *;

-- find students that are enrolled, older than 20 and are from oldest to youngest
SELECT * FROM students
WHERE enrollment_status AND student_age > 20
ORDER BY student_age DESC;