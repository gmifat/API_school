from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__, template_folder='views')

school_db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="fatmagmiden",
    database="school")



@app.route('/')
def hello_world():
    return 'app school'



@app.route('/test', methods=['GET'])
def test():
    return "toto"


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


@app.route('/teachers', methods=['GET'])
def get_all_teachers():
    school_cursor = school_db.cursor()
    school_cursor.execute("select subject_id, subject_name from subject")
    subjects = school_cursor.fetchall()
    school_cursor = school_db.cursor()
    school_cursor.execute("select teacher_id, first_name, last_name,grade,  email, address, phone from teacher ")
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('teachers.html', subjects=subjects, teachers=result)


@app.route('/teachers/<teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    school_cursor = school_db.cursor()
    school_cursor.execute("select teacher_id, first_name, last_name, grade, email, address, phone from teacher"
                          " where teacher_id = %(s_id)s",
                          {'s_id': teacher_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('teacher.html', teacher=result[0])


@app.route('/teachers/add', methods=['POST'])
def add_teacher():
    school_cursor = school_db.cursor()
    school_cursor.execute("insert into teacher (first_name, last_name, grade, email, phone, address)"
                          " values (%(v_first_name)s,%(v_last_name)s,%(v_grade)s,%(v_email)s,%(v_phone)s,"
                          " %(v_address)s)", {'v_first_name': request.form['teacher_name'],
                                              'v_last_name': request.form['teacher_lastName'],
                                              'v_grade': request.form['teacher_grade'],
                                              'v_email': request.form['teacher_email'],
                                              'v_phone': request.form['teacher_phone'],
                                              'v_address': request.form['teacher_address']})
    teacher_id = school_cursor.lastrowid
    subjects = request.form.getlist('subjects')
    for subject_id in subjects:
        school_cursor.execute("insert into speciality (teacher_id, subject_id) values(%(v_t_id)s, %(v_s_id)s)",
                              {'v_t_id': teacher_id, 'v_s_id': subject_id})
    school_db.commit()
    school_cursor.close()

    return redirect("/teachers")


@app.route('/teachers/update/<teacher_id>', methods=['GET'])
def get_teacher_to_update(teacher_id):
    school_cursor = school_db.cursor()
    school_cursor.execute("select teacher_id, first_name, last_name, grade, email, address, phone from teacher"
                          " where teacher_id = %(s_id)s",
                          {'s_id': teacher_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('teacher_update.html', teacher=result[0])


@app.route('/teachers/update', methods=['POST'])
def update_teacher():
    t_id = request.form['teacher_id']
    school_cursor = school_db.cursor()
    teacher = {'v_first_name': request.form['teacher_name'],
               'v_last_name': request.form['teacher_lastName'],
               'v_grade': request.form['teacher_grade'],
               'v_email': request.form['teacher_email'],
               'v_phone': request.form['teacher_phone'],
               'v_address': request.form['teacher_address'],
               'v_id': t_id}
    school_cursor.execute("update teacher set first_name = %(v_first_name)s, last_name = %(v_last_name)s,"
                          " grade = %(v_grade)s, email = %(v_email)s, phone = %(v_phone)s, address = %(v_address)s"
                          " where teacher_id = %(v_id)s", teacher)
    school_db.commit()
    school_cursor.close()
    return redirect("/teachers")


@app.route('/teachers/delete/<teacher_id>', methods=['GET'])
def get_teacher_to_delete(teacher_id):
    school_cursor = school_db.cursor()
    school_cursor.execute("select teacher_id, first_name, last_name, grade, email, address, phone from teacher"
                          " where teacher_id = %(s_id)s",
                          {'s_id': teacher_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('delete.html', teacher=result[0])


@app.route('/teachers/delete', methods=['POST'])
def delete_teacher():
    t_id = request.form['teacher_id']
    school_cursor = school_db.cursor()
    school_cursor.execute("delete from teacher  where teacher_id = (%(t_id)s)", {'t_id': t_id})
    school_db.commit()
    school_cursor.close()
    return redirect("/teachers")


########student


@app.route('/students', methods=['GET'])
def get_all_students():
    school_cursor = school_db.cursor()
    school_cursor.execute("select class_id, name from class")
    classes = school_cursor.fetchall()
    school_cursor.execute("select student.student_id, student.first_name, student.last_name, student.card_number,"
                          " class.name, student.email, student.address, student.phone from student"
                          " join class on class.class_id = student.class_id")
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('students.html', classes=classes, students=result)


@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    school_cursor = school_db.cursor()
    school_cursor.execute("select student.student_id, student.first_name, student.last_name, student.card_number,"
                          " class.name, student.email, student.address, student.phone from student"
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
    school_cursor.execute("select class_id, name from class")
    classes = school_cursor.fetchall()
    school_cursor.execute("select student.student_id, student.first_name, student.last_name, student.card_number,"
                          " class.name, student.email, student.address, student.phone, class.class_id from student"
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


@app.route('/admins', methods=['GET'])
def get_all_admins():
    school_cursor = school_db.cursor()
    school_cursor.execute("select admin_id, first_name, last_name, role, email, address, phone from administration")
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('admins.html', admins=result)


@app.route('/admins/<admin_id>', methods=['GET'])
def get_admin(admin_id):
    school_cursor = school_db.cursor()
    school_cursor.execute("select admin_id, first_name, last_name, role, email, address, phone from administration"
                          " where admin_id = %(sd_id)s", {'sd_id': admin_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('admin.html', admin=result[0])


@app.route('/admins/add', methods=['POST'])
def add_admin():
    school_cursor = school_db.cursor()
    school_cursor.execute("insert into administration (first_name, last_name, role, email, address, phone)"
                          " values (%(ad_first_name)s, %(ad_last_name)s, %(ad_role)s, %(ad_email)s, %(ad_address)s,"
                          " %(ad_phone)s)", {'ad_first_name': request.form['admin_name'],
                                             'ad_last_name': request.form['admin_lastName'],
                                             'ad_role': request.form['admin_role'],
                                             'ad_email': request.form['admin_email'],
                                             'ad_address': request.form['admin_address'],
                                             'ad_phone': request.form['admin_phone']})
    school_db.commit()
    school_cursor.close()
    return redirect('/admins')


@app.route('/admins/update/<admin_id>', methods=['GET'])
def get_admin_to_update(admin_id):
    school_cursor = school_db.cursor()
    school_cursor.execute("select admin_id, first_name, last_name, role, email, address, phone from administration"
                          " where admin_id = %(ad_id)s", {'ad_id': admin_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('admin_update.html', admin=result[0])


@app.route('/admins/update', methods=['POST'])
def update_admin():
    ad_id = request.form['admin_id']
    school_cursor = school_db.cursor()
    admin = {'ad_first_name': request.form['admin_name'],
             'ad_last_name': request.form['admin_lastName'],
             'ad_role': request.form['admin_role'],
             'ad_email': request.form['admin_email'],
             'ad_address': request.form['admin_address'],
             'ad_phone': request.form['admin_phone'],
             'ad_id': ad_id}
    school_cursor.execute("update administration set first_name = %(ad_first_name)s, last_name = %(ad_last_name)s,"
                          " role =  %(ad_role)s, email = %(ad_email)s, address = %(ad_address)s, phone = %(ad_phone)s"
                          " where admin_id = %(ad_id)s", admin)
    school_db.commit()
    school_cursor.close()
    return redirect("/admins")


app.run(debug=True)
