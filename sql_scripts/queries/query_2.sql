-- Find the student with the highest average grade in the given discipline.
SELECT  d.discipline_name,
        s.first_name || ' ' || s.last_name AS student_name,
        ROUND(AVG(g.grade), 2) AS avg_grade
FROM    grades g
JOIN    students s ON g.student_id = s.id
JOIN    disciplines d ON g.discipline_id = d.id
WHERE   d.id = 1  -- 'Python Core'
GROUP BY student_name
ORDER BY avg_grade DESC
LIMIT 1;