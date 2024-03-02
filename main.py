from faker import Faker
import psycopg2
import random

faker = Faker()

conn_params = "dbname='your_db_name' user='your_db_user' host='localhost' password='your_db_password'"
conn = psycopg2.connect(conn_params)
cur = conn.cursor()

group_names = ['A', 'B', 'C']
group_ids = []
for name in group_names:
    cur.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id;", (name,))
    group_id = cur.fetchone()[0]
    group_ids.append(group_id)

teacher_names = [faker.name() for _ in range(5)]
teacher_ids = []
for name in teacher_names:
    cur.execute("INSERT INTO teachers (name) VALUES (%s) RETURNING id;", (name,))
    teacher_id = cur.fetchone()[0]
    teacher_ids.append(teacher_id)

subject_names = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'English']
subject_ids = []
for name in subject_names:
    teacher_id = random.choice(teacher_ids)
    cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s) RETURNING id;", (name, teacher_id))
    subject_id = cur.fetchone()[0]
    subject_ids.append(subject_id)

for _ in range(50):
    name = faker.name()
    group_id = random.choice(group_ids)
    cur.execute("INSERT INTO students (name, group_id) VALUES (%s, %s) RETURNING id;", (name, group_id))
    student_id = cur.fetchone()[0]
    
    for subject_id in subject_ids:
        for _ in range(random.randint(5, 20)):
            grade = random.randint(1, 10)
            date_received = faker.date_between(start_date='-2y', end_date='today')
            cur.execute("INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (%s, %s, %s, %s);",
                        (student_id, subject_id, grade, date_received))

conn.commit()
cur.close()
conn.close()
