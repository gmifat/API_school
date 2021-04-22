
app = Flask(__name__, template_folder='views')

school_db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="fatmagmiden",
    database="school"
)
########student


@app.route('/students', methods=['GET'])
def get_all_student():
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
