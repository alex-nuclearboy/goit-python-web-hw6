-- Find a list of students in the specific group.
SELECT  g.group_name as "Group",
        s.first_name || ' ' || s.last_name AS "Student"
FROM    students s
JOIN    groups g ON s.group_id = g.id
WHERE   g.id = 2;  -- 'PyWeb20-2'