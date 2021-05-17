from collections import defaultdict

from flask import render_template, request, redirect
from base import app
from base import school_db


@app.route('/class_sessions/<class_id>', methods=['GET'])
def get_class_sessions(class_id):
    school_cursor = school_db.cursor()
    school_cursor.execute("select class.class_id, class.class_name,class_subject.subject_id, subject.subject_name,"
                          " class_subject.class_subject_id"
                          " from class left join class_subject on class.class_id = class_subject.class_id"
                          " left join subject on class_subject.subject_id = subject.subject_id"
                          " where class.class_id = %(cl_id)s",
                          {'cl_id': class_id})
    class_info = school_cursor.fetchall()
    school_cursor.execute("select speciality.speciality_id,"
                          " tc.teacher_id, tc.first_name, tc.last_name, sb.subject_id, sb.subject_name"
                          " from teacher tc"
                          " join speciality on speciality.teacher_id = tc.teacher_id"
                          " join subject sb on speciality.subject_id = sb.subject_id"
                          " order by tc.teacher_id")
    teacher_info = school_cursor.fetchall()
    school_cursor.execute("select classroom_id, room_number from classroom order by room_number")
    classrooms = school_cursor.fetchall()

    school_cursor.execute("select cls.class_session_id, cls.speciality_id, cls.class_subject_id,"
                          " cls.day, TIME_FORMAT(cls.start_time, '%H:%i'), TIME_FORMAT(cls.end_time, '%H:%i'),"
                          " cls.videoconference,"
                          " teacher.teacher_id, teacher.first_name, teacher.last_name,"
                          " subject.subject_id, subject.subject_name,"
                          " cls.classroom_id, classroom.room_number"
                          " from class_session cls"
                          " join speciality on speciality.speciality_id = cls.speciality_id"
                          " join class_subject on class_subject.class_subject_id = cls.class_subject_id"
                          " join subject on speciality.subject_id = subject.subject_id"
                          " join teacher on speciality.teacher_id = teacher.teacher_id"
                          " left join classroom on classroom.classroom_id = cls.classroom_id"
                          " where class_subject.class_id = %(cl_id)s"
                          " order by day, cls.start_time", {'cl_id': class_id})
    class_sessions = school_cursor.fetchall()
    grp_class_sessions = defaultdict(list)
    for class_session in class_sessions:
        grp_class_sessions[class_session[3]].append(class_session)

    school_cursor.close()
    return render_template('class_session/class_session.html', class_info=class_info, teacher_info=teacher_info,
                           classrooms=classrooms, class_sessions=grp_class_sessions)


@app.route('/class_sessions', methods=['POST'])
def add_class_sessions():
    school_cursor = school_db.cursor()
    try:
        classroom_id = request.form['classroom_id']
        if classroom_id == 'no_classroom':
            classroom_id = None

        school_cursor.execute("insert into class_session (speciality_id, class_subject_id, classroom_id,"
                              " day, start_time, end_time, videoconference)"
                              " values (%(speciality_id)s, %(class_subject_id)s, %(classroom_id)s,"
                              " %(day)s, %(start_time)s, %(end_time)s, %(videoconference)s)",
                              {
                                'speciality_id': request.form['speciality_id'],
                                'class_subject_id': request.form['class_subject_id'],
                                'classroom_id': classroom_id,
                                'day': request.form['day'],
                                'start_time': request.form['start_time'],
                                'end_time': request.form['end_time'],
                                'videoconference': request.form['videoconference']
                              })
        school_db.commit()
    except:
        req = school_cursor.statement
        print(req)

    school_cursor.close()
    return redirect('/class_sessions/'+request.form['class_id'])


@app.route('/class_sessions/<class_id>/<class_session_id>', methods=['GET'])
def get_class_sessions_to_update(class_id, class_session_id):
    school_cursor = school_db.cursor()
    school_cursor.execute("select class.class_id, class.class_name,class_subject.subject_id, subject.subject_name,"
                          " class_subject.class_subject_id"
                          " from class left join class_subject on class.class_id = class_subject.class_id"
                          " left join subject on class_subject.subject_id = subject.subject_id"
                          " where class.class_id = %(cl_id)s",
                          {'cl_id': class_id})
    class_info = school_cursor.fetchall()
    school_cursor.execute("select speciality.speciality_id,"
                          " tc.teacher_id, tc.first_name, tc.last_name, sb.subject_id, sb.subject_name"
                          " from teacher tc"
                          " join speciality on speciality.teacher_id = tc.teacher_id"
                          " join subject sb on speciality.subject_id = sb.subject_id"
                          " order by tc.teacher_id")
    teacher_info = school_cursor.fetchall()
    school_cursor.execute("select classroom_id, room_number from classroom order by room_number")
    classrooms = school_cursor.fetchall()

    school_cursor.execute("select cls.class_session_id, cls.speciality_id, cls.class_subject_id,"
                          " cls.day, TIME_FORMAT(cls.start_time, '%H:%i'), TIME_FORMAT(cls.end_time, '%H:%i'),"
                          " cls.videoconference,"
                          " teacher.teacher_id, teacher.first_name, teacher.last_name,"
                          " subject.subject_id, subject.subject_name,"
                          " cls.classroom_id, classroom.room_number"
                          " from class_session cls"
                          " join speciality on speciality.speciality_id = cls.speciality_id"
                          " join class_subject on class_subject.class_subject_id = cls.class_subject_id"
                          " join subject on speciality.subject_id = subject.subject_id"
                          " join teacher on speciality.teacher_id = teacher.teacher_id"
                          " left join classroom on classroom.classroom_id = cls.classroom_id"
                          " where class_subject.class_id = %(cl_id)s"
                          " order by day, cls.start_time", {'cl_id': class_id})
    class_sessions = school_cursor.fetchall()
    grp_class_sessions = defaultdict(list)
    class_session_to_update = None
    for class_session in class_sessions:
        grp_class_sessions[class_session[3]].append(class_session)
        if class_session[0] == int(class_session_id):
            class_session_to_update = class_session

    school_cursor.close()
    return render_template('class_session/class_session.html', class_info=class_info, teacher_info=teacher_info,
                           classrooms=classrooms, class_sessions=grp_class_sessions,
                           class_session_to_update=class_session_to_update)


@app.route('/class_sessions/update', methods=['POST'])
def update_class_sessions():
    #school_cursor = school_db.cursor()
    #school_cursor.execute("select ")
    return redirect()


@app.route('/class_sessions/delete/<class_session_id>', methods=['GET'])
def get_class_sessions_to_delete(class_session_id):
    #school_cursor = school_db.cursor()
    #school_cursor.execute("select ")

    return class_session_id
