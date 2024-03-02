CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    group_id INT
);

CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    student_id INT,
    subject_id INT,
    grade INT,
    date_received DATE,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);
