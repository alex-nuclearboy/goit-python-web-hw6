-- Find the grades of students in the given group in the specific discipline.
SELECT  d.discipline_name as "Discipline",
        gp.group_name as "Group",
        s.first_name || ' ' || s.last_name AS "Student",
        gr.grade as "Grade",
        gr.grade_date as "Date"
FROM    students s
JOIN    grades gr ON gr.student_id = s.id
JOIN    disciplines d ON gr.discipline_id = d.id
JOIN    groups gp ON s.group_id = gp.id
WHERE   (
        d.id = 5  -- 'Databases and SQL'
        AND gp.id = 1  -- 'PyWeb20-1'
        )
ORDER BY "Student";