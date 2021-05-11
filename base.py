from flask import Flask, render_template, request, redirect
import mysql.connector


app = Flask(__name__, template_folder='views')

school_db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="fatmagmiden",
    database="school")

