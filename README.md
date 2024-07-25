# University Management System

## Overview
This project is a Flask-based web application designed to manage various aspects of a university. It uses an SQLite database to store and retrieve information about students, professors, lessons, enrollments, educational groups, books, libraries, and educational staff. The application provides routes to display data and perform specific queries.

## Features
- **Home Page**: Displays the main page.
- **Students**: View all students.
- **Professors**: View all professors.
- **Lessons**: View all lessons.
- **Enrollments**: View all enrollments.
- **Educational Groups**: View all educational groups.
- **Books**: View all books.
- **Libraries**: View all libraries.
- **Educational Staff**: View all educational staff.

### Query Routes
- **/query/student_enrollments**: Students who have enrolled in lessons.
- **/query/lessons_more_than_five_students**: Lessons with more than five students.
- **/query/student_avg_grades**: Students' average grades.
- **/query/professors_more_than_70_units**: Professors teaching more than 70 units.
- **/query/books_borrowed_by_more_than_four**: Books borrowed by more than four students.
- **/query/professor_schedule**: Professors' schedules based on specific conditions.
- **/query/students_without_lessons**: Students registered but not enrolled in any lessons.

## Setup Instructions
1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/university-management-system.git
    ```
2. Navigate to the project directory:
    ```sh
    cd university-management-system
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the Flask application:
    ```sh
    python app.py
    ```

## Database Setup
To set up the SQLite database with initial tables and data, execute the following steps:
1. Open a Python shell or a new script file.
2. Execute the provided database setup code to create tables and insert sample data.

## Routes
- **/**: Home page.
- **/students**: View all students.
- **/professors**: View all professors.
- **/lessons**: View all lessons.
- **/enrollments**: View all enrollments.
- **/educational_groups**: View all educational groups.
- **/books**: View all books.
- **/libraries**: View all libraries.
- **/educational_staff**: View all educational staff.
- **/test_db**: Test database connection and view table data.
- **/add_sample_data**: Add sample data to the database.

## Query Routes
- **/query/student_enrollments**: Students who have enrolled in lessons.
- **/query/lessons_more_than_five_students**: Lessons with more than five students.
- **/query/student_avg_grades**: Students' average grades.
- **/query/professors_more_than_70_units**: Professors teaching more than 70 units.
- **/query/books_borrowed_by_more_than_four**: Books borrowed by more than four students.
- **/query/professor_schedule**: Professors' schedules based on specific conditions.
- **/query/students_without_lessons**: Students registered but not enrolled in any lessons.

## Logging
Logging is set up to provide debug information, helping trace the application's execution and identify issues.

## Contributing
Feel free to fork this repository and submit pull requests. Any enhancements or bug fixes are welcome.

## License
This project is licensed under the MIT License.
<a href="https://nowpayments.io/donation?api_key=REWCYVC-A1AMFK3-QNRS663-PKJSBD2&source=lk_donation&medium=referral" target="_blank">
     <img src="https://nowpayments.io/images/embeds/donation-button-black.svg" alt="Crypto donation button by NOWPayments">
    </a>
