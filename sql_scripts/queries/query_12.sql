-- Find the grades of students in the particular group in the given subject in the last class.
SELECT  gp.group_name AS "Group",
        d.discipline_name AS "Discipline",
        s.first_name || ' ' || s.last_name AS "Student",
        gr.grade AS "Grade",
        MAX(gr.grade_date) AS "Date of the last grade"
FROM    grades gr
JOIN    disciplines d ON gr.discipline_id = d.id
JOIN    students s ON gr.student_id = s.id
JOIN    groups gp ON s.group_id = gp.id
WHERE   (
        gp.id = 3    -- 'PyWeb20-3'
        AND d.id = 1 -- 'Python Core'
        )
GROUP BY "Student"
ORDER BY "Student";