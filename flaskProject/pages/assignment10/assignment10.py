from flask import Flask, render_template, redirect, url_for, request, session, Blueprint, jsonify
import mysql.connector

assignment10 = Blueprint('assignment10', __name__, static_folder='static',
                          static_url_path='/ex10', template_folder='templates')


@assignment10.route("/ex10")
def usersList():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)


@assignment10.route("/ex10insert", methods=['GET', 'POST'])
def insert_user():
    name = request.form['name']
    nickname = request.form['nickname']
    query = "insert into users(name, nickname) values ('%s', '%s')" % (name, nickname)
    interact_db(query=query, query_type='commit')
    return redirect('/ex10')


@assignment10.route("/ex10delete", methods=['POST'])
def delete_user():
    name = request.form['name']
    query = "delete from users where name='%s';" % name
    interact_db(query, query_type='commit')
    return redirect("/ex10")


@assignment10.route("/ex10update", methods=['POST'])
def update_user():
    name = request.form['name']
    nickname = request.form['nickname']
    query = "update users set nickname = '%s' where name='%s';" % (nickname, name)
    interact_db(query, query_type='commit')
    return redirect("/ex10")


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

