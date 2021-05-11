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
