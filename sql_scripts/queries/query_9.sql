-- Find a list of disciplines the particular student is taking.
SELECT DISTINCT s.first_name || ' ' || s.last_name AS "Student",
        d.discipline_name AS "Discipline"
FROM    grades g
JOIN    students s ON g.student_id = s.id
JOIN    disciplines d ON g.discipline_id = d.id
WHERE   s.id = 10;