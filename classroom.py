from flask import render_template, request, redirect
from base import app
from base import school_db


@app.route('/classrooms', methods=['GET'])
def get_all_classrooms():
    school_cursor = school_db.cursor()
    school_cursor.execute("select classroom_id, room_number from classroom")
    classrooms = school_cursor.fetchall()
    school_cursor.close()
    return render_template('classroom/classrooms.html', classrooms=classrooms)


def get_classroom_details(classroom_id, classroom_details):
    school_cursor = school_db.cursor()
    school_cursor.execute("select classroom_id, room_number from classroom where classroom_id = %(s_id)s",
                          {'s_id': classroom_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template(classroom_details, classroom=result[0])


@app.route('/classrooms/<classroom_id>', methods=['GET'])
def get_classroom(classroom_id):
    return get_classroom_details(classroom_id, 'classroom/classroom.html')


@app.route('/classrooms/add', methods=['POST'])
def add_classroom():
    room_number = request.form['classroom_name']
    school_cursor = school_db.cursor()
    school_cursor.execute("insert into classroom (room_number) values (%(name)s)", {'name': room_number})
    school_db.commit()
    school_cursor.close()
    return redirect("/classrooms")


@app.route('/classrooms/update/<classroom_id>', methods=['GET'])
def get_classroom_to_update(classroom_id):
    return get_classroom_details(classroom_id, 'classroom/classroom_update.html')


@app.route('/classrooms/update', methods=['POST'])
def update_classroom():
    classroom = request.form['classroom_name']
    cl_id = request.form['classroom_id']
    school_cursor = school_db.cursor()
    classroom_data = {'name': classroom, 'id': cl_id}
    school_cursor.execute("update classroom set room_number = %(name)s where classroom_id = %(id)s", classroom_data)
    school_db.commit()
    school_cursor.close()
    return redirect("/classrooms")


@app.route('/classrooms/delete/<classroom_id>', methods=['GET'])
def get_classroom_to_delete(classroom_id):
    return get_classroom_details(classroom_id, 'classroom/classroom_delete.html')


@app.route('/classrooms/delete', methods=['POST'])
def delete_classroom():
    classroom_data = request.form['classroom_id']
    school_cursor = school_db.cursor()
    school_cursor.execute("delete from classroom  where classroom_id = (%(cl_id)s)", {'cl_id': classroom_data})
    school_db.commit()
    school_cursor.close()
    return redirect("/classrooms")

