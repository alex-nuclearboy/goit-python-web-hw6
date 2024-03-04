DROP TABLE IF EXISTS grades CASCADE;
DROP TABLE IF EXISTS disciplines CASCADE;
DROP TABLE IF EXISTS teachers CASCADE;
DROP TABLE IF EXISTS students CASCADE;
DROP TABLE IF EXISTS groups CASCADE;

-- Creating groups table
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    group_name VARCHAR(10) NOT NULL
);

-- Creating students table with a foreign key referencing groups
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES groups(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Creating teachers table
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

-- Creating disciplines table with a foreign key referencing teachers
CREATE TABLE disciplines (
    id SERIAL PRIMARY KEY,
    discipline_name VARCHAR(50) NOT NULL,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Creating grades table with foreign keys referencing students and disciplines
CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    discipline_id INT NOT NULL,
    grade INT CHECK (grade BETWEEN 1 AND 5),
    grade_date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (discipline_id) REFERENCES disciplines(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
