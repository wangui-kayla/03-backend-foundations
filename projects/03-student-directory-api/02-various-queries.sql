-- show every student
SELECT * FROM students;

-- show only strudents enrolled in certain courses
SELECT * FROM students
WHERE student_course = 'Bachelor of Science in Computer Science';

SELECT * FROM students
WHERE student_course = 'Bachelor of Architecture';

SELECT * FROM students
WHERE student_course = 'Bachelor of Education (Arts)';

-- show students older than 20 years
SELECT * FROM students
WHERE student_age > 20;

-- show only enrolled students
SELECT * FROM students
WHERE enrollment_status;

-- show only not enrolled students
SELECT * FROM students
WHERE NOT enrollment_status;

-- show students from youngest to oldest
SELECT * FROM students
ORDER BY student_age ASC;

-- show students from oldest to youngest who are enrolled
SELECT * FROM students
WHERE enrollment_status
ORDER BY student_age DESC;

-- change a student's course and verify the change
UPDATE students
SET student_course = 'Bachelor of Science in Computer Science'
WHERE student_name = 'Joy Wambui'
RETURNING *;

-- delete one student then show all
DELETE FROM students
WHERE student_name = 'Brian Kiprop';

SELECT * FROM students;