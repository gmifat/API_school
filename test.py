import mysql.connector

school_db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="fatmagmiden",
  database="school"
)


school_cursor = school_db.cursor()
school_cursor.execute("select * from subject")
result = school_cursor.fetchall()
print(result)
school_cursor.close()
