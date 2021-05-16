insert into class_session
(speciality_id, class_subject_id, classroom_id, day, start_time, end_time, virtual)
values ('30', '19', '11', 'Vendredi', '08:30', '10:00', '')




school_cursor.execute("select cls.class_session_id, cls.speciality_id, cls.class_subject_id,"
                          " cls.day, cls.start_time, cls.duration, cls.virtual, subject.subject_name,"
                          " teacher.*, classroom.*"
                          " from class_session cls"
                          " join speciality on speciality.speciality_id = cls.speciality_id"
                          " join class_subject on class_subject.class_subject_id = cls.class_subject_id"
                          " join subject on speciality.subject_id = subject.subject_id"
                          " join teacher on speciality.teacher_id = teacher.teacher_id"
                          " left join classroom on classroom.classroom_id = cls.classroom_id"
                          " where class_subject.class_id = %(cl_id)s"
                          " order by day", {'cl_id': class_id})
    class_sessions = school_cursor.fetchall()




























list = [(1, 's'), (2, 'f'), (3, 'l')]
#print(list)
for item in list:
    print(str(item[0]) + ' ' + item[1])



select student.student_id, student.first_name, student.last_name, student.card_number,"
                          " class.name, student.email, student.address, student.phone from student




select student_id, first_name, last_name, card_number, class_id,"
                          " email, address, phone from student


@app.route('/students', methods=['GET'])
def get_all_student():
    school_cursor = school_db.cursor()
    school_cursor.execute("select student_id, first_name,last_name, card_number, class_id,"
                          " email, address, phone from student ")
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('students.html', students=result)

