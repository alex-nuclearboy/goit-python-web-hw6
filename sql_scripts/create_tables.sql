CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(10)  NOT NULL
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(150)  NOT NULL,
    group_id INTEGER REFERENCES groups(id)
    ON DELETE CASCADE
);

CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(150)  NOT NULL
);

CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)  NOT NULL,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    student_id INT,
    subject_id INT,
    grade INT CHECK (grade BETWEEN 1 AND 5),
    date_received DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);
