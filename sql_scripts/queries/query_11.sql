-- Find the average grade that the given teacher gives to the particular student.
SELECT  t.first_name || ' ' || t.last_name AS "Teacher",
        s.first_name || ' ' || s.last_name AS "Student",
        ROUND(AVG(g.grade), 2) as "Average grade"
FROM    grades g
JOIN    students s ON g.student_id = s.id
JOIN    disciplines d ON g.discipline_id = d.id
JOIN    teachers t ON d.teacher_id = t.id
WHERE   (
        s.id = 25
        AND t.id = 5
        );