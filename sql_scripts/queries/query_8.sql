-- Find the average grade given by the particular teacher in their disciplines.
SELECT  t.first_name || ' ' || t.last_name AS "Teacher",
        ROUND(AVG(g.grade), 2) AS "Average grade"
FROM    grades g
JOIN    disciplines d ON g.discipline_id = d.id
JOIN    teachers t ON d.teacher_id = t.id
WHERE   t.id = 1;