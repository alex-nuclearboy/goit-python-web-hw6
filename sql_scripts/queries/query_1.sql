-- Find the 5 students with the highest average grade in all disciplines.
SELECT  s.first_name || ' ' || s.last_name as student_name,
        ROUND(AVG(g.grade), 2) AS avg_grade
FROM    students s
JOIN    grades g ON s.id = g.student_id
GROUP BY student_name
ORDER BY avg_grade DESC
LIMIT 5;