-- Find the average grade for the course (across whole full grade table).
SELECT  ROUND(AVG(g.grade), 2) AS avg_grade
FROM    grades g;