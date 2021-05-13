from flask import render_template, request, redirect
from base import app
from base import school_db


@app.route('/students', methods=['GET'])
def get_all_students():
    school_cursor = school_db.cursor()
    school_cursor.execute("select class_id, class_name from class")
    classes = school_cursor.fetchall()
    school_cursor.execute("select student.student_id, student.first_name, student.last_name, student.card_number,"
                          " class.class_name, student.email, student.address, student.phone from student"
                          " join class on class.class_id = student.class_id order by last_name")
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('student/students.html', classes=classes, students=result)


def get_student_details(student_id, student_template):
    school_cursor = school_db.cursor()
    school_cursor.execute("select student.student_id, student.first_name, student.last_name, student.card_number,"
                          " class.class_name, student.email, student.address, student.phone from student"
                          " join class on class.class_id = student.class_id"
                          " where student_id = %(st_id)s", {'st_id': student_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template(student_template, student=result[0])


@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    return get_student_details(student_id, 'student/student.html')


@app.route('/students/add', methods=['POST'])
def add_student():
    school_cursor = school_db.cursor()
    school_cursor.execute("insert into student (first_name, last_name, card_number, class_id, email, address, phone)"
                          " values(%(st_first_name)s, %(st_last_name)s, %(st_card_number)s,%(st_class)s, %(st_email)s,"
                          " %(st_address)s,%(st_phone)s)", {'st_first_name': request.form['student_name'],
                                                            'st_last_name': request.form['student_lastName'],
                                                            'st_card_number': request.form['student_card'],
                                                            'st_class': request.form['student_class'],
                                                            'st_email': request.form['student_email'],
                                                            'st_address': request.form['student_address'],
                                                            'st_phone': request.form['student_phone']})
    school_db.commit()
    school_cursor.close()
    return redirect('/students')


@app.route('/students/update/<student_id>', methods=['GET'])
def get_student_to_update(student_id):
    school_cursor = school_db.cursor()
    school_cursor.execute("select class_id, class_name from class")
    classes = school_cursor.fetchall()
    school_cursor.execute("select student.student_id, student.first_name, student.last_name, student.card_number,"
                          " class.class_name, student.email, student.address, student.phone, class.class_id"
                          " from student"
                          " join class on class.class_id = student.class_id"
                          " where student_id = %(st_id)s", {'st_id': student_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('student/student_update.html', student=result[0], classes=classes)


@app.route('/students/update', methods=['POST'])
def update_student():
    school_cursor = school_db.cursor()
    st_id = request.form['student_id']

    student = {'st_first_name': request.form['student_name'],
               'st_last_name': request.form['student_lastName'],
               'st_card_number': request.form['student_card'],
               'st_class': request.form['student_class'],
               'st_email': request.form['student_email'],
               'st_address': request.form['student_address'],
               'st_phone': request.form['student_phone'],
               'st_id': st_id}
    school_cursor.execute("update student set first_name = %(st_first_name)s, last_name = %(st_last_name)s,"
                          " card_number = %(st_card_number)s, class_id = %(st_class)s,"
                          " email = %(st_email)s, address = %(st_address)s, phone = %(st_phone)s"
                          " where student_id = %(st_id)s", student)
    school_db.commit()
    school_cursor.close()
    return redirect('/students')


@app.route('/students/delete/<student_id>', methods=['GET'])
def get_student_to_delete(student_id):
    return get_student_details(student_id, 'student/student_delete.html')


@app.route('/students/delete', methods=['POST'])
def delete_student():
    st_id = request.form['student_id']
    school_cursor = school_db.cursor()
    school_cursor.execute("delete from student  where student_id = (%(st_id)s)", {'st_id': st_id})
    school_db.commit()
    school_cursor.close()
    return redirect("/students")


@app.route('/students/mark/<student_id>', methods=['GET'])
def get_student_marks(student_id):
    return "In progress"


