from flask import Flask, jsonify, request,  abort
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect('postgresql://user1:hheezziiee@localhost/user1')
cursor = conn.cursor()

cursor.execute('''create table if not exists users(user_id serial,
               username varchar, password varchar);''')
cursor.execute('''select * from users;''')
users = cursor.fetchall()
conn.commit()


def taken_username(username):
    try:
        cursor.execute('''select username from users where username='{}';'''
                       .format(username))
        taken_user = cursor.fetchall()
        print(taken_user)
        conn.commit()
        if taken_user[0][0] == username:
            return True
    except Exception as e:
        print(e)
        return False


@app.route('/')
def first_flask_app():
    return jsonify({
        "status": 200,
        "message": "Hello world"}), 200


@app.route('/users', methods=['POST'])
def create_users():

    response = request.get_json()
    if not response:
        return jsonify(
            {
                "status": 400,
                "message": "Please provide json data"
            }
        ), 400
        abort
    username = response['username']
    password = response['password']
    if not username or not password:
        return jsonify(
            {
                "status": 400,
                "message": "Please fill all the fields"
            }
        ), 400
        abort
    if taken_username(username):
        return jsonify(
            {
                "status": 400,
                "message": "The username is already taken"
            }
        ), 400
        abort
    if len(password) < 6:
        return jsonify(
            {
                "status": 400,
                "message": "Please provide a valid password"
            }
        ), 400
        abort
    try:
        cursor.execute('''insert into users
                       (username, password) values('{}','{}');'''
                       .format(username, password))
        cursor.execute('''select * from users where username='{}';'''
                       .format(username))
        user = cursor.fetchall()
        conn.commit()
        return jsonify({
            "status": 201,
            "message": "user created successfully",
            "data": user
        }), 201
    except Exception as e:
        print(e)


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({
        "status": 200,
        "message": "Users successfully fetched",
        "data": users
    }), 200


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cursor.execute('''select * from users where user_id='{}';'''
                   .format(user_id))
    user = cursor.fetchall()
    conn.commit()
    return jsonify({
        "status": 200,
        "message":
        "user with id {} fetched succesfully".format(user_id),
        "data": user
    }), 200


@app.route('/username/<int:user_id>', methods=['PATCH'])
def edit_username(user_id):
    response = request.get_json()
    if not response:
        return jsonify(
            {
                "status": 400,
                "message": "Please provide json data"
            }
        ), 400
        abort
    username = response['username']
    if not username:
        return jsonify(
            {
                "status": 400,
                "message": "Please fill all the fields"
            }
        ), 400
        abort
    if taken_username(username):
        return jsonify(
            {
                "status": 400,
                "message": "The username is already taken"
            }
        ), 400
        abort
    try:
        cursor.execute("""UPDATE users SET username ='{}' where user_id={};"""
                       .format(username, user_id))
        cursor.execute('''select * from users where username='{}';'''
                       .format(username))
        user = cursor.fetchall()
        conn.commit()
        return jsonify({
            "status": 201,
            "message": "user edited successfully",
            "data": user
        }), 201
    except Exception as e:
        print(e)


@app.route('/password/<int:user_id>', methods=['PATCH'])
def edit_password(user_id):
    response = request.get_json()
    if not response:
        return jsonify(
            {
                "status": 400,
                "message": "Please provide json data"
            }
        ), 400
        abort
    password = response['password']
    if not password:
        return jsonify(
            {
                "status": 400,
                "message": "Please fill all the fields"
            }
        ), 400
        abort
    try:
        cursor.execute("""UPDATE users SET password ='{}' where user_id={};"""
                       .format(password, user_id))
        cursor.execute('''select * from users where password='{}';'''
                       .format(password))
        user = cursor.fetchall()
        conn.commit()
        return jsonify({
            "status": 201,
            "message": "password edited successfully",
            "data": user
        }), 201
    except Exception as e:
        print(e)


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cursor.execute('''delete from users where user_id='{}';'''
                   .format(user_id))
    conn.commit()
    return jsonify({
        "status": 200,
        "message": "User successfully deleted"
    }), 200



if __name__ == "__main__":
    app.run(debug=True)
