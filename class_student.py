from flask import render_template, request, redirect
from base import app
from base import school_db


@app.route('/classes', methods=['GET'])
def get_all_classes():

    school_cursor = school_db.cursor()
    school_cursor.execute("select subject_id, subject_name from subject order by subject_name")
    subjects = school_cursor.fetchall()
    school_cursor.execute("select class_id, class_name from class order by class_name")
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('class/classes.html', classes=result, subjects=subjects)


def get_class_details(class_id, class_template):
    school_cursor = school_db.cursor()
    school_cursor.execute("select class.class_id, class.class_name,class_subject.subject_id, subject.subject_name"
                          " from class left join class_subject on class.class_id = class_subject.class_id"
                          " left join subject on class_subject.subject_id = subject.subject_id"
                          " where class.class_id = %(s_id)s",
                          {'s_id': class_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template(class_template, classes=result[0], class_details=result)


@app.route('/classes/<class_id>', methods=['GET'])
def get_class(class_id):
    return get_class_details(class_id, 'class/class_view.html')


@app.route('/classes/add', methods=['POST'])
def add_class():
    name = request.form['class_name']
    school_cursor = school_db.cursor()
    school_cursor.execute("insert into class (class_name) values (%(name)s)", {'name': name})

    class_id = school_cursor.lastrowid
    subjects = request.form.getlist('subjects')
    for subject_id in subjects:
        school_cursor.execute("insert into class_subject (class_id, subject_id) values(%(cl_id)s, %(sb_id)s)",
                              {'cl_id': class_id, 'sb_id': subject_id})
    school_db.commit()
    school_cursor.close()
    return redirect("/classes")


@app.route('/classes/update/<class_id>', methods=['GET'])
def get_class_to_update(class_id):
    return get_class_details(class_id, 'class/class_update.html')


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


@app.route('/classes/delete/<class_id>', methods=['GET'])
def get_class_to_delete(class_id):
    return get_class_details(class_id, 'class/class_delete.html')

