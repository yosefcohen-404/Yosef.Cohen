from flask import Flask, render_template, redirect, url_for, request, session, jsonify
import mysql.connector
from pages.assignment10.assignment10 import assignment10

app = Flask(__name__)
app.secret_key = '123'

app.register_blueprint(assignment10)


@app.route('/')
def hello_world():
    return render_template("cv.html")


@app.route('/Full cv')
def full_cv():
    return render_template("Full cv page.html")


@app.route('/Contact List')
def cl():
    return render_template("Contact list page.html")


@app.route('/Projects')
def proj():
    return render_template("Projects page.html")


@app.route('/Contact me')
def cm():
    return render_template("Contact me page.html")


@app.route('/assignment8')
def a8():
    return render_template("assignment8.html", name="", hobbies=["Sports", "Reading", "Doing this assignment"])


@app.route('/assignment8b')
def a8ext():
    return render_template("blockA8.html", name="", hobbies=["Sports", "Reading", "Doing this assignment"])


@app.route('/assignment9', methods=["GET", "POST"])
def a9():
    curr_method = request.method
    users = {"Dan111": "Dani", "Davie504": "David", "Avi19": "Avi"}
    user_name = ''
    user_name_src = ''

    if curr_method == "GET":
        if 'user_name_src' in request.args:
            user_name_src = request.args['user_name_src']
        else:
            user_name_src = ''
    elif curr_method == "POST":
        if 'user_name' in request.form:
            user_name = request.form['user_name']
        else:
            user_name = ''
        if user_name in users:
            session['user_nickname'] = users[user_name]
        else:
            session['user_nickname'] = ''
    else:
        user_name, user_name_src = '', ''

    return render_template("assignment9.html",
                           users=users,
                           user_name=user_name,
                           curr_method=curr_method,
                           user_name_src=user_name_src)


@app.route("/logout")
def logout():
    session['user_nickname'] = ''
    return redirect('/assignment9')


@app.route("/assignment11/users")
def assign11_users():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    response = "no data in users table"
    if len(query_result) != 0:
        response = query_result
    response = jsonify(response)

    return response


@app.route("/assignment11/users/selected", defaults={'user_id': 1})
@app.route("/assignment11/users/selected/<int:user_id>")
def assign11_select_user(user_id):
    query = "select * from users where user_id='%s';" % user_id
    query_result = interact_db(query=query, query_type='fetch')
    response = "please enter a correct user id"
    if len(query_result) != 0:
        response = query_result
    response = jsonify(response)

    return response


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='web')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


if __name__ == '__main__':
    app.run()
