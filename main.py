from flask import render_template, request, redirect

# import declared routes
import admin
import teacher
import student
import classroom
import subject
import class_student
import class_session

from base import app
from base import school_db


@app.route('/')
def host_api():
    return render_template('home.html')


app.run(debug=True)
