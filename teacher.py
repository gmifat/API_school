from flask import render_template, request, redirect
from base import app
from base import school_db


@app.route('/teachers', methods=['GET'])
def get_all_teachers():
    school_cursor = school_db.cursor()
    school_cursor.execute("select subject_id, subject_name from subject")
    subjects = school_cursor.fetchall()
    school_cursor = school_db.cursor()
    school_cursor.execute("select teacher_id, first_name, last_name,grade,  email, address, phone from teacher ")
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('teacher/teachers.html', subjects=subjects, teachers=result)


def get_teacher_details(teacher_id, teacher_template):
    school_cursor = school_db.cursor()
    school_cursor.execute("select tc.teacher_id, tc.first_name, tc.last_name, tc.grade, tc.email, tc.address,"
                          " tc.phone, sb.subject_id, sb.subject_name from teacher tc"
                          " left join speciality on speciality.teacher_id = tc.teacher_id"
                          " left join subject sb on speciality.subject_id = sb.subject_id"
                          " where tc.teacher_id = %(s_id)s",
                          {'s_id': teacher_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template(teacher_template, teacher=result[0], teacher_details=result)


@app.route('/teachers/<teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    return get_teacher_details(teacher_id, 'teacher/teacher.html')


@app.route('/teachers/delete/<teacher_id>', methods=['GET'])
def get_teacher_to_delete(teacher_id):
    return get_teacher_details(teacher_id, 'teacher/teacher_delete.html')


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
    school_cursor.execute("select subject.subject_id, subject.subject_name, speciality.teacher_id from subject"
                          " left join speciality on speciality.subject_id = subject.subject_id"
                          " where speciality.teacher_id is null or speciality.teacher_id = %(t_id)s",
                          {'t_id': teacher_id})
    subjects = school_cursor.fetchall()
    school_cursor.execute("select teacher_id, first_name, last_name, grade, email, address, phone from teacher"
                          " where teacher_id = %(t_id)s",
                          {'t_id': teacher_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('teacher/teacher_update.html', teacher=result[0], subjects=subjects)


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


@app.route('/teachers/delete', methods=['POST'])
def delete_teacher():
    t_id = request.form['teacher_id']
    school_cursor = school_db.cursor()
    school_cursor.execute("delete from teacher  where teacher_id = (%(t_id)s)", {'t_id': t_id})
    school_db.commit()
    school_cursor.close()
    return redirect("/teachers")
