import sqlite3

# Connect to the database (or create it)
conn = sqlite3.connect('student_record.db')
# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create students table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS student_record (
                    Enrollment INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    Subject TEXT NOT NULL,
                    Mark INTEGER NOT NULL
                )''')

# Commit the changes
conn.commit()

# Insert multiple employee records
student_record = [
    (92301733016, 'ASHUTOSH KUMAR SINGH', 'PWP', 95),
    (92301733017, 'HARSH VISHALBHAI TRIVEDI', 'PWP', 85),
    (92301733027, 'VIRAJ PRAKASHBHAI VAGHASIYA', 'PWP', 90),
    (92301733046, 'SHIVAM ATULKUMAR BHATT', 'PWP', 93),
    (92301733058, 'DEVENDRASINH DOLATSINH JADEJA', 'PWP', 75)
]

# Check for duplicates before inserting
for record in student_record:
    cursor.execute("SELECT * FROM student_record WHERE Enrollment = ?", (record[0],))
    result = cursor.fetchone()
    if result is None:  # Insert only if the record doesn't exist
        cursor.execute('''INSERT INTO student_record (Enrollment, name, Subject, Mark) 
                          VALUES (?, ?, ?, ?)''', record)
    else:
        print(f"Enrollment {record[0]} already exists. Skipping insert for {record[1]}.")

# Commit the changes
conn.commit()
# Calculate the average Mark
cursor.execute('''SELECT AVG(Mark) FROM student_record''')
avg_mark = cursor.fetchone()[0]

print(f"\nThe average mark of students is: ${avg_mark:.2f}")
# Close the connection
conn.close()

