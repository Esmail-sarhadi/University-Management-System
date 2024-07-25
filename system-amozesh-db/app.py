from flask import Flask, request, jsonify, render_template
import sqlite3
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

def get_db_connection():
    conn = sqlite3.connect('university.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/students', methods=['GET'])
def get_students():
    try:
        conn = get_db_connection()
        students = conn.execute('SELECT * FROM student').fetchall()
        conn.close()
        app.logger.info(f'Retrieved {len(students)} students')
        return render_template('students.html', students=students)
    except Exception as e:
        app.logger.error(f'Error retrieving students: {str(e)}')
        return f'Error: {str(e)}', 500

@app.route('/professors', methods=['GET'])
def get_professors():
    try:
        conn = get_db_connection()
        professors = conn.execute('SELECT * FROM professor').fetchall()
        conn.close()
        app.logger.info(f'Retrieved {len(professors)} professors')
        return render_template('professors.html', professors=professors)
    except Exception as e:
        app.logger.error(f'Error retrieving professors: {str(e)}')
        return f'Error: {str(e)}', 500

@app.route('/lessons', methods=['GET'])
def get_lessons():
    try:
        conn = get_db_connection()
        lessons = conn.execute('SELECT * FROM lesson').fetchall()
        conn.close()
        app.logger.info(f'Retrieved {len(lessons)} lessons')
        return render_template('lessons.html', lessons=lessons)
    except Exception as e:
        app.logger.error(f'Error retrieving lessons: {str(e)}')
        return f'Error: {str(e)}', 500

@app.route('/enrollments', methods=['GET'])
def get_enrollments():
    try:
        conn = get_db_connection()
        enrollments = conn.execute('SELECT * FROM enrollment').fetchall()
        conn.close()
        app.logger.info(f'Retrieved {len(enrollments)} enrollments')
        return render_template('enrollments.html', enrollments=enrollments)
    except Exception as e:
        app.logger.error(f'Error retrieving enrollments: {str(e)}')
        return f'Error: {str(e)}', 500

@app.route('/educational_groups', methods=['GET'])
def get_educational_groups():
    try:
        conn = get_db_connection()
        educational_groups = conn.execute('SELECT * FROM educational_group').fetchall()
        conn.close()
        app.logger.info(f'Retrieved {len(educational_groups)} educational groups')
        return render_template('educational_groups.html', educational_groups=educational_groups)
    except Exception as e:
        app.logger.error(f'Error retrieving educational groups: {str(e)}')
        return f'Error: {str(e)}', 500

@app.route('/books', methods=['GET'])
def get_books():
    try:
        conn = get_db_connection()
        books = conn.execute('SELECT * FROM book').fetchall()
        conn.close()
        app.logger.info(f'Retrieved {len(books)} books')
        return render_template('books.html', books=books)
    except Exception as e:
        app.logger.error(f'Error retrieving books: {str(e)}')
        return f'Error: {str(e)}', 500

@app.route('/libraries', methods=['GET'])
def get_libraries():
    try:
        conn = get_db_connection()
        libraries = conn.execute('SELECT * FROM library').fetchall()
        conn.close()
        app.logger.info(f'Retrieved {len(libraries)} libraries')
        return render_template('libraries.html', libraries=libraries)
    except Exception as e:
        app.logger.error(f'Error retrieving libraries: {str(e)}')
        return f'Error: {str(e)}', 500

@app.route('/educational_staff', methods=['GET'])
def get_educational_staff():
    try:
        conn = get_db_connection()
        staff = conn.execute('SELECT * FROM educational_staff').fetchall()
        conn.close()
        app.logger.info(f'Retrieved {len(staff)} educational staff members')
        return render_template('educational_staff.html', staff=staff)
    except Exception as e:
        app.logger.error(f'Error retrieving educational staff: {str(e)}')
        return f'Error: {str(e)}', 500

@app.route('/query/student_enrollments')
def student_enrollments():
    conn = get_db_connection()
    query = '''
    SELECT DISTINCT student_number 
    FROM enrollment
    '''
    result = conn.execute(query).fetchall()
    conn.close()
    return render_template('query_result.html', title="Students who have enrolled", result=result)

@app.route('/query/lessons_more_than_five_students')
def lessons_more_than_five_students():
    conn = get_db_connection()
    query = '''
    SELECT lesson_code 
    FROM enrollment
    GROUP BY lesson_code
    HAVING COUNT(DISTINCT student_number) > 5
    '''
    result = conn.execute(query).fetchall()
    conn.close()
    return render_template('query_result.html', title="Lessons with more than 5 students", result=result)

@app.route('/query/student_avg_grades')
def student_avg_grades():
    conn = get_db_connection()
    query = '''
    SELECT e.student_number, AVG(e.grade * l.course) / SUM(l.course) as weighted_avg
    FROM enrollment e
    JOIN lesson l ON e.lesson_code = l.lesson_code
    GROUP BY e.student_number
    '''
    result = conn.execute(query).fetchall()
    conn.close()
    return render_template('query_result.html', title="Student average grades", result=result)

@app.route('/query/professors_more_than_70_units')
def professors_more_than_70_units():
    conn = get_db_connection()
    query = '''
    SELECT p.master_code, p.firstname, p.lastname, SUM(l.course) as total_units
    FROM professor p
    JOIN lesson l ON p.master_code = l.professor_code
    GROUP BY p.master_code
    HAVING SUM(l.course) > 70
    '''
    result = conn.execute(query).fetchall()
    conn.close()
    columns = ['master_code', 'firstname', 'lastname', 'total_units'] if result else []
    return render_template('query_result.html', title="Professors teaching more than 70 units", result=result, columns=columns)

@app.route('/query/books_borrowed_by_more_than_four')
def books_borrowed_by_more_than_four():
    conn = get_db_connection()
    query = '''
    SELECT b.book_name
    FROM book b
    JOIN library_book lb ON b.book_code = lb.book_code
    GROUP BY b.book_code
    HAVING COUNT(DISTINCT lb.student_number) > 4
    '''
    result = conn.execute(query).fetchall()
    conn.close()
    return render_template('query_result.html', title="Books borrowed by more than 4 students", result=result)

@app.route('/query/professor_schedule')
def professor_schedule():
    conn = get_db_connection()
    query = '''
    SELECT p.master_code, p.firstname, p.lastname, l.lesson_code, l.course
    FROM professor p
    JOIN lesson l ON p.master_code = l.professor_code
    WHERE l.lesson_code IN (
        SELECT lesson_code
        FROM enrollment
        GROUP BY lesson_code
        HAVING COUNT(DISTINCT student_number) > 20
    )
    GROUP BY p.master_code
    HAVING COUNT(DISTINCT l.lesson_code) >= 3
    '''
    result = conn.execute(query).fetchall()
    conn.close()
    return render_template('query_result.html', title="Professor schedule with conditions", result=result)

@app.route('/query/students_without_lessons')
def students_without_lessons():
    conn = get_db_connection()
    query = '''
    SELECT s.student_number, s.firstname, s.lastname
    FROM student s
    LEFT JOIN enrollment e ON s.student_number = e.student_number
    WHERE e.student_number IS NULL
    '''
    result = conn.execute(query).fetchall()
    conn.close()
    return render_template('query_result.html', title="Students registered but not enrolled in any lessons", result=result)

@app.route('/test_db')
def test_db():
    conn = get_db_connection()
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    data = {}
    for table in tables:
        table_name = table['name']
        rows = conn.execute(f'SELECT * FROM {table_name}').fetchall()
        data[table_name] = [dict(row) for row in rows]
    conn.close()
    return jsonify(data)

@app.route('/add_sample_data')
def add_sample_data():
    conn = get_db_connection()
    conn.execute('''INSERT INTO student (student_number, phone_number, firstname, lastname, email, enrollment_code)
                    VALUES (1, 1234567890, 'John', 'Doe', 'john@example.com', 1),
                           (2, 2345678901, 'Jane', 'Smith', 'jane@example.com', 2)''')
    conn.commit()
    conn.close()
    return 'Sample data added'

if __name__ == '__main__':
    app.run(debug=True)
