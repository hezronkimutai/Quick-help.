from flask import Flask, jsonify, request,  abort

app = Flask(__name__)

users = []


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
    for user in users:
        if username in user.values():
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
    new_user = {
        "user_id": len(users)+1,
        "username": username,
        "password": password
    }
    users.append(new_user)
    return jsonify({
        "status": 201,
        "message": "user created successfully",
        "data": new_user
    }), 201


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({
        "status": 200,
        "message": "Users successfully fetched",
        "data": users
    }), 200


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user_id in user.values():
            return jsonify({
                "status": 200,
                "message":
                "user with id {} fetched succesfully".format(user_id),
                "data": user
            }), 200


@app.route('/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    for user in users:
        if user_id in user.values():
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
            for user in users:
                if username in user.values():
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
            user['username'] = username
            user['password'] = password
            return jsonify({
                "status": 201,
                "message": "User edited succesfully"
            }), 201


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user_id in user.values():
            del users[user_id]
            return jsonify({
                "status": 200,
                "message": "User successfully deleted"
            }), 200


if __name__ == "__main__":
    app.run(debug=True)
