







































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

