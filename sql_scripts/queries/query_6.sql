-- Find a list of students in the specific group.
SELECT  g.group_name,
        s.first_name || ' ' || s.last_name AS student_name
FROM    students s
JOIN    groups g ON s.group_id = g.id
WHERE   g.id = 2;  -- 'PyWeb20-2'