from flask import render_template, request, redirect
from base import app
from base import school_db


@app.route('/admins', methods=['GET'])
def get_all_admins():
    school_cursor = school_db.cursor()
    school_cursor.execute("select admin_id, first_name, last_name, role, email, address, phone from administration")
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('admin/admins.html', admins=result)


def get_admin_details(admin_id, admin_template):
    school_cursor = school_db.cursor()
    school_cursor.execute("select admin_id, first_name, last_name, role, email, address, phone from administration"
                          " where admin_id = %(sd_id)s", {'sd_id': admin_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template(admin_template, admin=result[0])


@app.route('/admins/<admin_id>', methods=['GET'])
def get_admin(admin_id):
    return get_admin_details(admin_id, 'admin/admin.html')


@app.route('/admins/delete/<admin_id>', methods=['GET'])
def get_admin_for_delete(admin_id):
    return get_admin_details(admin_id, 'admin/admin_delete.html')


@app.route('/admins/add', methods=['POST'])
def add_admin():
    school_cursor = school_db.cursor()
    school_cursor.execute("insert into administration (first_name, last_name, role, email, address, phone)"
                          " values (%(ad_first_name)s, %(ad_last_name)s, %(ad_role)s, %(ad_email)s, %(ad_address)s,"
                          " %(ad_phone)s)", {'ad_first_name': request.form['admin_name'],
                                             'ad_last_name': request.form['admin_lastName'],
                                             'ad_role': request.form['admin_role'],
                                             'ad_email': request.form['admin_email'],
                                             'ad_address': request.form['admin_address'],
                                             'ad_phone': request.form['admin_phone']})
    school_db.commit()
    school_cursor.close()
    return redirect('/admins')


@app.route('/admins/update/<admin_id>', methods=['GET'])
def get_admin_to_update(admin_id):
    school_cursor = school_db.cursor()
    school_cursor.execute("select admin_id, first_name, last_name, role, email, address, phone from administration"
                          " where admin_id = %(ad_id)s", {'ad_id': admin_id})
    result = school_cursor.fetchall()
    school_cursor.close()
    return render_template('admin/admin_update.html', admin=result[0])


@app.route('/admins/update', methods=['POST'])
def update_admin():
    ad_id = request.form['admin_id']
    school_cursor = school_db.cursor()
    admin = {'ad_first_name': request.form['admin_name'],
             'ad_last_name': request.form['admin_lastName'],
             'ad_role': request.form['admin_role'],
             'ad_email': request.form['admin_email'],
             'ad_address': request.form['admin_address'],
             'ad_phone': request.form['admin_phone'],
             'ad_id': ad_id}
    school_cursor.execute("update administration set first_name = %(ad_first_name)s, last_name = %(ad_last_name)s,"
                          " role =  %(ad_role)s, email = %(ad_email)s, address = %(ad_address)s, phone = %(ad_phone)s"
                          " where admin_id = %(ad_id)s", admin)
    school_db.commit()
    school_cursor.close()
    return redirect("/admins")


@app.route('/admins/delete', methods=['POST'])
def delete_admin():
    ad_id = request.form['admin_id']
    school_cursor = school_db.cursor()
    school_cursor.execute("delete from administration  where admin_id = (%(a_id)s)", {'a_id': ad_id})
    school_db.commit()
    school_cursor.close()
    return redirect("/admins")
