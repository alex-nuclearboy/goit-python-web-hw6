-- Find the average grade in groups for the given discipline.
SELECT  d.discipline_name,
        gp.group_name,
        ROUND(AVG(gr.grade), 2) AS avg_grade
FROM    grades gr
JOIN    students s ON gr.student_id = s.id
JOIN    disciplines d ON gr.discipline_id = d.id
JOIN    groups gp ON s.group_id = gp.id
WHERE   d.id = 5  -- 'Databases and SQL'
GROUP BY gp.group_name
ORDER BY avg_grade DESC;