-- Find what disciplines the particular teacher teaches.
SELECT  t.first_name || ' ' || t.last_name AS teacher_name,
        d.discipline_name as discipline
FROM    teachers t
JOIN    disciplines d ON d.teacher_id = t.id
WHERE   t.id = 5;