from flask import render_template, request, redirect
from base import app
from base import school_db


@app.route('/marks', methods=['GET'])
def get_all_marks():
    school_cursor = school_db.cursor()
    school_cursor.execute("select mark_id, score_value from mark")

    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('mark/marks.html', admins=result)
