import sqlite3

# اتصال به پایگاه داده
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# ساخت جداول
cursor.execute('''CREATE TABLE IF NOT EXISTS student (
                    student_number INTEGER PRIMARY KEY,
                    phone_number INTEGER,
                    firstname TEXT,
                    lastname TEXT,
                    email TEXT,
                    enrollment_code INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS professor (
                    master_code INTEGER PRIMARY KEY,
                    position TEXT,
                    national_code INTEGER,
                    firstname TEXT,
                    lastname TEXT,
                    email TEXT,
                    phone_number INTEGER,
                    educational_group_code INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS lesson (
                    lesson_code INTEGER PRIMARY KEY,
                    course INTEGER,
                    professor_code INTEGER,
                    FOREIGN KEY (professor_code) REFERENCES professor(master_code))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS enrollment (
                    enrollment_code INTEGER PRIMARY KEY,
                    student_number INTEGER,
                    lesson_code INTEGER,
                    grade REAL,
                    enrollment_date TEXT,
                    educational_group_code INTEGER,
                    employee_code INTEGER,
                    FOREIGN KEY (student_number) REFERENCES student(student_number),
                    FOREIGN KEY (lesson_code) REFERENCES lesson(lesson_code))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS educational_group (
                    group_code INTEGER PRIMARY KEY,
                    group_name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS book (
                    book_code INTEGER PRIMARY KEY,
                    book_name TEXT,
                    publication_year INTEGER,
                    pages INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS library (
                    library_code INTEGER PRIMARY KEY,
                    address TEXT,
                    name TEXT,
                    number_of_books INTEGER,
                    university_address TEXT,
                    employee_code INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS educational_staff (
                    employee_code INTEGER PRIMARY KEY,
                    firstname TEXT,
                    lastname TEXT,
                    phone_number INTEGER,
                    educational_group_code INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS library_book (
                    book_code INTEGER,
                    student_number INTEGER,
                    FOREIGN KEY (book_code) REFERENCES book(book_code),
                    FOREIGN KEY (student_number) REFERENCES student(student_number))''')

# داده‌های اصلاح شده
students = [
    (1, 1234567890, 'John', 'Doe', 'john@example.com', 1),
    (2, 2345678901, 'Jane', 'Smith', 'jane@example.com', 2),
    (3, 3456789012, 'Jim', 'Brown', 'jim@example.com', 3),
    (4, 4567890123, 'Jake', 'White', 'jake@example.com', 4),
    (5, 5678901234, 'Jill', 'Black', 'jill@example.com', 5),
    (6, 6789012345, 'Joan', 'Green', 'joan@example.com', 6),
    (7, 7890123456, 'Jeff', 'Blue', 'jeff@example.com', 7),
    (8, 8901234567, 'Jess', 'Red', 'jess@example.com', 8),
    (9, 9012345678, 'Jay', 'Yellow', 'jay@example.com', 9),
    (10, 1012345678, 'Judy', 'Purple', 'judy@example.com', 10),
    (11, 1112345678, 'Jack', 'Orange', 'jack@example.com', 11)  # دانشجویی که هیچ واحدی را انتخاب نکرده است
]

professors = [
    (1, 'Professor', 1111111111, 'Alice', 'Brown', 'alice@example.com', 1111111111, 1),
    (2, 'Associate Professor', 2222222222, 'Bob', 'Smith', 'bob@example.com', 2222222222, 2),
    (3, 'Assistant Professor', 3333333333, 'Charlie', 'Jones', 'charlie@example.com', 3333333333, 3),
    (4, 'Lecturer', 4444444444, 'David', 'Garcia', 'david@example.com', 4444444444, 4),
    (5, 'Professor', 5555555555, 'Eve', 'Martinez', 'eve@example.com', 5555555555, 5)
]

lessons = [
    (1, 4, 1), (2, 4, 1), (3, 4, 1), (4, 4, 1), (500, 4, 1),  # استاد 1، 80 واحد تدریس می‌کند
    (6, 3, 2), (7, 3, 2), (8, 3, 2), (9, 3, 2), (10, 3, 2),  # استاد 2، 75 واحد تدریس می‌کند
    (11, 3, 3), (12, 3, 3), (13, 3, 3), (14, 3, 3), (15, 3, 3)  # استاد 3، 75 واحد تدریس می‌کند
]

enrollments = [
    (1, 1, 1, 18, '2024-01-01', 1, 1),
    (2, 2, 2, 16, '2024-01-01', 2, 2),
    (3, 3, 3, 19, '2024-01-01', 3, 3),
    (4, 4, 4, 20, '2024-01-01', 4, 4),
    (5, 5, 5, 15, '2024-01-01', 5, 5),
    (6, 6, 6, 14, '2024-01-01', 6, 6),
    (7, 7, 7, 13, '2024-01-01', 7, 7),
    (8, 8, 8, 17, '2024-01-01', 8, 8),
    (9, 9, 9, 19, '2024-01-01', 9, 9),
    (10, 10, 10, 20, '2024-01-01', 10, 10),
    (11, 1, 11, 18, '2024-01-01', 1, 1),
    (12, 2, 12, 16, '2024-01-01', 2, 2),
    (13, 3, 13, 19, '2024-01-01', 3, 3),
    (14, 4, 14, 20, '2024-01-01', 4, 4),
    (15, 5, 15, 15, '2024-01-01', 5, 5)
]
educational_groups = [
    (1, 'Computer Science'),
    (2, 'Mathematics'),
    (3, 'Physics'),
    (4, 'Chemistry'),
    (5, 'Biology')
]

books = [
    (1, 'Data Structures', 2020, 500),
    (2, 'Algorithms', 2019, 450),
    (3, 'Operating Systems', 2018, 600),
    (4, 'Database Systems', 2017, 550),
    (5, 'Artificial Intelligence', 2021, 400)
]

libraries = [
    (1, 'Main St, City', 'Central Library', 10000, '123 University St, City', 1),
    (2, '2nd St, City', 'North Library', 8000, '123 University St, City', 1),
    (3, '3rd St, City', 'East Library', 6000, '123 University St, City', 2),
    (4, '4th St, City', 'West Library', 4000, '123 University St, City', 3),
    (5, '5th St, City', 'South Library', 2000, '123 University St, City', 4)
]

educational_staff = [
    (1, 'Michael', 'Clark', 1111111111, 1),
    (2, 'Sarah', 'Davis', 2222222222, 2),
    (3, 'Thomas', 'Lopez', 3333333333, 3),
    (4, 'Karen', 'Wilson', 4444444444, 4),
    (5, 'James', 'Taylor', 5555555555, 5)
]

library_books = [
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
    (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
    (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
    (4, 1), (4, 2), (4, 3), (4, 4), (4, 5),
    (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)
]

# درج داده‌ها در جداول
cursor.executemany('INSERT INTO student VALUES (?, ?, ?, ?, ?, ?)', students)
cursor.executemany('INSERT INTO professor VALUES (?, ?, ?, ?, ?, ?, ?, ?)', professors)
cursor.executemany('INSERT INTO lesson VALUES (?, ?, ?)', lessons)
cursor.executemany('INSERT INTO enrollment VALUES (?, ?, ?, ?, ?, ?, ?)', enrollments)
cursor.executemany('INSERT INTO educational_group VALUES (?, ?)', educational_groups)
cursor.executemany('INSERT INTO book VALUES (?, ?, ?, ?)', books)
cursor.executemany('INSERT INTO library VALUES (?, ?, ?, ?, ?, ?)', libraries)
cursor.executemany('INSERT INTO educational_staff VALUES (?, ?, ?, ?, ?)', educational_staff)
cursor.executemany('INSERT INTO library_book VALUES (?, ?)', library_books)

# تایید تغییرات و بستن اتصال به پایگاه داده
conn.commit()
conn.close()

print("okeye :)")
