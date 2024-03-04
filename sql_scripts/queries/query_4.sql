-- Find the average grade for the course (across whole full grade table).
SELECT  ROUND(AVG(g.grade), 2) AS "Average grade"
FROM    grades g;