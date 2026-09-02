CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
	student_name VARCHAR(50) NOT NULL UNIQUE,
	student_age INTEGER NOT NULL,
	student_course VARCHAR(60) NOT NULL,
	enrollment_status BOOLEAN DEFAULT true
);

INSERT INTO students (student_name, student_age, student_course, enrollment_status)
VALUES
    ('Brian Kiprop', 21, 'Bachelor of Science in Nursing', true),
	('Amina Wanjiku', 20, 'Bachelor of Science in Computer Science', true),
	('Kevin Odhiambo', 22, 'Bachelor of Education (Arts)', true),
	('Mercy Chebet', 19, 'Bachelor of Commerce', true),
	('David Mutua', 23, 'Bachelor of Laws (LL.B)', true),
	('Sharon Akinyi', 21, 'Bachelor of Architecture', true),
	('Emmanuel Kiprono', 20, 'Bachelor of Science in Civil Engineering', false),
	('Joy Wambui', 22, 'Bachelor of Pharmacy', true),
	('Abdi Rahman', 24, 'Bachelor of Economics and Statistics', true),
	('Faith Mwende', 21, 'Bachelor of Journalism and Mass Communication', false)
ON CONFLICT (student_name) DO NOTHING;