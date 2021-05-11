from flask import render_template, request, redirect

# import declared routes
import admin
import teacher
import student

from base import app
from base import school_db


@app.route('/')
def host_api():
    return render_template('home.html')


########subject


@app.route('/subjects', methods=['GET'])
def get_all_subjects():
    school_cursor = school_db.cursor()
    school_cursor.execute("select subject_id, subject_name from subject")
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('subjects.html', subjects=result)


@app.route('/subjects/<subject_id>', methods=['GET'])
def get_subject(subject_id):
    school_cursor = school_db.cursor()
    school_cursor.execute("select subject_id, subject_name from subject where subject_id = %(s_id)s",
                          {'s_id': subject_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('subject.html', subject=result[0])


@app.route('/subjects/add', methods=['POST'])
def add_subject():
    data = request.form['subject_name']
    school_cursor = school_db.cursor()
    school_cursor.execute("insert into subject (subject_name) values (%(name)s)", {'name': data})
    school_db.commit()
    school_cursor.close()
    return redirect("/subjects")


@app.route('/subjects/update', methods=['POST'])
def update_subject():
    data = request.form['subject_name']
    s_id = request.form['subject_id']
    school_cursor = school_db.cursor()
    subject = {'name': data, 'id': s_id}
    school_cursor.execute("update subject set subject_name = %(name)s where subject_id = %(id)s", subject)
    school_db.commit()
    school_cursor.close()
    return redirect("/subjects")


@app.route('/subjects/delete', methods=['POST'])
def delete_subject():
    data = request.form['subject_id']
    school_cursor = school_db.cursor()
    school_cursor.execute("delete from subject  where subject_id = (%(s_id)s)", {'s_id': data})
    school_db.commit()
    school_cursor.close()
    return redirect("/subjects")


########teachers





########student


@app.route('/students', methods=['GET'])
def get_all_students():
    school_cursor = school_db.cursor()
    school_cursor.execute("select class_id, class_name from class")
    classes = school_cursor.fetchall()
    school_cursor.execute("select student.student_id, student.first_name, student.last_name, student.card_number,"
                          " class.class_name, student.email, student.address, student.phone from student"
                          " join class on class.class_id = student.class_id")
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('students.html', classes=classes, students=result)


@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    school_cursor = school_db.cursor()
    school_cursor.execute("select student.student_id, student.first_name, student.last_name, student.card_number,"
                          " class.class_name, student.email, student.address, student.phone from student"
                          " join class on class.class_id = student.class_id"
                          " where student_id = %(st_id)s", {'st_id': student_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('student.html', student=result[0])


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
    return render_template('student_update.html', student=result[0], classes=classes)


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


########admin

########class


@app.route('/classes', methods=['GET'])
def get_all_classes():
    school_cursor = school_db.cursor()
    school_cursor.execute("select class_id, class_name from class")
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('classes.html', classes=result)


@app.route('/classes/<class_id>', methods=['GET'])
def get_class(class_id):
    school_cursor = school_db.cursor()
    school_cursor.execute("select class_id, class_name from class where class_id = %(s_id)s",
                          {'s_id': class_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('class_view.html', classes=result[0])


@app.route('/classes/add', methods=['POST'])
def add_class():
    name = request.form['class_name']
    school_cursor = school_db.cursor()
    school_cursor.execute("insert into class (class_name) values (%(name)s)", {'name': name})
    school_db.commit()
    school_cursor.close()
    return redirect("/classes")


@app.route('/classes/update', methods=['POST'])
def update_class():
    student_class = request.form['class_name']
    cl_id = request.form['class_id']
    school_cursor = school_db.cursor()
    class_data = {'name': student_class, 'id': cl_id}
    school_cursor.execute("update class set class_name = %(name)s where class_id = %(id)s", class_data)
    school_db.commit()
    school_cursor.close()
    return redirect("/classes")


########classroom


@app.route('/classrooms', methods=['GET'])
def get_all_classrooms():
    school_cursor = school_db.cursor()
    school_cursor.execute("select classroom_id, room_number from classroom")
    classrooms = school_cursor.fetchall()
    school_cursor.close()
    return render_template('classrooms.html', classrooms=classrooms)


@app.route('/classrooms/<classroom_id>', methods=['GET'])
def get_classroom(classroom_id):
    school_cursor = school_db.cursor()
    school_cursor.execute("select classroom_id, room_number from classroom where classroom_id = %(s_id)s",
                          {'s_id': classroom_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('classroom.html', classroom=result[0])


@app.route('/classrooms/add', methods=['POST'])
def add_classroom():
    room_number = request.form['classroom_name']
    school_cursor = school_db.cursor()
    school_cursor.execute("insert into classroom (room_number) values (%(name)s)", {'name': room_number})
    school_db.commit()
    school_cursor.close()
    return redirect("/classrooms")


app.run(debug=True)
