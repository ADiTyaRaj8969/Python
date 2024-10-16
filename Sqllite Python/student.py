import sqlite3

# Connect to the database (or create it)
conn = sqlite3.connect('student_record.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create the 'students' table
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    Enrollment INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                )''')

# Create the 'subjects' table
cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    subject_name TEXT NOT NULL
                )''')

# Create the 'student_enrollment' table to store the many-to-many relationship
cursor.execute('''CREATE TABLE IF NOT EXISTS student_enrollment (
                    Enrollment INTEGER,
                    subject_id INTEGER,
                    Mark INTEGER NOT NULL,
                    FOREIGN KEY (Enrollment) REFERENCES students(Enrollment),
                    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
                    PRIMARY KEY (Enrollment, subject_id)
                )''')

# Commit the changes
conn.commit()

# Insert multiple student records (without subjects, only name and Enrollment)
students = [
    (92301733016, 'ASHUTOSH KUMAR SINGH'),
    (92301733017, 'HARSH VISHALBHAI TRIVEDI'),
    (92301733027, 'VIRAJ PRAKASHBHAI VAGHASIYA'),
    (92301733046, 'SHIVAM ATULKUMAR BHATT'),
    (92301733058, 'DEVENDRASINH DOLATSINH JADEJA')
]

# Insert subjects (subject_name only)
subjects = [
    ('PWP',),
    ('Math',),
    ('Physics',)
]

# Insert student records (check for duplicates)
for student in students:
    cursor.execute("SELECT * FROM students WHERE Enrollment = ?", (student[0],))
    result = cursor.fetchone()
    if result is None:  # Insert only if the student doesn't exist
        cursor.execute('''INSERT INTO students (Enrollment, name) 
                          VALUES (?, ?)''', student)
    else:
        print(f"Enrollment {student[0]} already exists. Skipping insert for {student[1]}.")

# Insert subjects (check for duplicates by subject_name)
for subject in subjects:
    cursor.execute("SELECT * FROM subjects WHERE subject_name = ?", (subject[0],))
    result = cursor.fetchone()
    if result is None:  # Insert only if the subject doesn't exist
        cursor.execute('''INSERT INTO subjects (subject_name) 
                          VALUES (?)''', subject)
    else:
        print(f"Subject {subject[0]} already exists. Skipping insert.")

# Insert student subject enrollment (with marks)
student_enrollment = [
    (92301733016, 'PWP', 95),
    (92301733016, 'Math', 88),
    (92301733017, 'PWP', 85),
    (92301733027, 'Physics', 92),
    (92301733046, 'PWP', 93),
    (92301733058, 'PWP', 75),
    (92301733058, 'Math', 80)
]

# Get subject_id from subjects table and insert into student_enrollment
for enrollment in student_enrollment:
    cursor.execute("SELECT subject_id FROM subjects WHERE subject_name = ?", (enrollment[1],))
    subject_id = cursor.fetchone()
    
    if subject_id:
        cursor.execute('''SELECT * FROM student_enrollment 
                          WHERE Enrollment = ? AND subject_id = ?''', (enrollment[0], subject_id[0]))
        result = cursor.fetchone()
        if result is None:  # Insert only if the enrollment doesn't exist
            cursor.execute('''INSERT INTO student_enrollment (Enrollment, subject_id, Mark) 
                              VALUES (?, ?, ?)''', (enrollment[0], subject_id[0], enrollment[2]))
        else:
            print(f"Student {enrollment[0]} already enrolled in {enrollment[1]}. Skipping insert.")

# Commit the changes
conn.commit()

# Calculate the average Mark across all students and subjects
cursor.execute('''SELECT AVG(Mark) FROM student_enrollment''')
avg_mark = cursor.fetchone()[0]

print(f"\nThe average mark of students across all subjects is: {avg_mark:.2f}")

# Close the connection
conn.close()
