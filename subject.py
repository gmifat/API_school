from flask import render_template, request, redirect
from base import app
from base import school_db


@app.route('/subjects', methods=['GET'])
def get_all_subjects():
    school_cursor = school_db.cursor()
    school_cursor.execute("select subject_id, subject_name from subject order by subject_name")
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('subject/subjects.html', subjects=result)


def get_subject_details(subject_id, subject_template):
    school_cursor = school_db.cursor()
    school_cursor.execute("select subject_id, subject_name from subject where subject_id = %(s_id)s",
                          {'s_id': subject_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template(subject_template, subject=result[0])


@app.route('/subjects/<subject_id>', methods=['GET'])
def get_subject(subject_id):
    return get_subject_details(subject_id, 'subject/subject.html')


@app.route('/subjects/add', methods=['POST'])
def add_subject():
    data = request.form['subject_name']
    school_cursor = school_db.cursor()
    school_cursor.execute("insert into subject (subject_name) values (%(name)s)", {'name': data})
    school_db.commit()
    school_cursor.close()
    return redirect("/subjects")


@app.route('/subjects/update/<subject_id>', methods=['GET'])
def get_subject_to_update(subject_id):
    return get_subject_details(subject_id, 'subject/subject_update.html')


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


@app.route('/subjects/delete/<subject_id>', methods=['GET'])
def get_subject_to_delete(subject_id):
    return get_subject_details(subject_id, 'subject/subject_delete.html')


@app.route('/subjects/delete', methods=['POST'])
def delete_subject():
    data = request.form['subject_id']
    school_cursor = school_db.cursor()
    school_cursor.execute("delete from subject  where subject_id = (%(s_id)s)", {'s_id': data})
    school_db.commit()
    school_cursor.close()
    return redirect("/subjects")

