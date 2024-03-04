-- Find the 5 students with the highest average grade in all disciplines.
SELECT  s.first_name || ' ' || s.last_name as "Student",
        ROUND(AVG(g.grade), 2) AS "Average grade"
FROM    students s
JOIN    grades g ON s.id = g.student_id
GROUP BY "Student name"
ORDER BY "Average grade" DESC
LIMIT 5;