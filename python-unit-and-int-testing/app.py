import sqlite3
from flask import Flask, jsonify, request
import os


######################################
#
#  Functions used for unit tests
#
######################################

def calculate_factorial(number):
    factorial_number = 1
    for i in range(number):
        factorial_number = factorial_number * (i+1)
    return factorial_number


def get_user(user_id):
    connection = sqlite3.connect('example.db')
    item = connection.execute(
        f'SELECT * FROM users WHERE id = {user_id}').fetchone()
    return {
        "user_id": item[0],
        "name": item[1]
    }


######################################
#
#  App used for Integration tests
#
######################################

def create_app(name):
    app = Flask(name)
    database_filename = os.environ.get('DATABASE_FILENAME', 'my_db.db')
    db_connection = sqlite3.connect(database_filename, check_same_thread=False)

    app.config.from_mapping(
        DATABASE_CON=db_connection
    )

    @app.get('/users')
    def get_all_users():
        db_connection = app.config["DATABASE_CON"]
        db_connection.row_factory = sqlite3.Row
        cur = db_connection.cursor()
        cur.execute(
            "SELECT * FROM users"
        )
        data = cur.fetchall()
        return jsonify([
            {
                "user_id": element['user_id'],
                "username": element['username'],
                "full_name": element['fullname']
            }
            for element in data
        ])

    @app.post('/users')
    def create_user():
        """
          POST /users JSON
          {
            "username": string
            "fullname": string
          }
        """
        request_body = request.get_json()
        username = request_body["username"]
        fullname = request_body["fullname"]
        db_connection = app.config["DATABASE_CON"]
        cur = db_connection.cursor()
        cur.execute(
            "INSERT INTO users (username, fullname) VALUES (?,?)",
            (username, fullname)
        )
        db_connection.commit()
        user_id = cur.lastrowid
        db_connection.row_factory = sqlite3.Row
        cur = db_connection.cursor()
        cur.execute(
            "SELECT * FROM users where user_id =?", (user_id, )
        )
        data = cur.fetchone()
        dict_data = dict(data)
        return {
            'user_id': dict_data['user_id'],
            'username': dict_data['username'],
            'full_name': dict_data['fullname']
        }

    @app.delete('/users/<string:user_id>')
    def delete_user(user_id):
        db_connection = app.config["DATABASE_CON"]
        cur = db_connection.cursor()
        cur.execute('DELETE FROM users where user_id = ?', (user_id,))
        if cur.rowcount == 0:
            return {
                "message": "User not deleted successfully"
            }
        elif cur.rowcount == 1:
            return {
                "message": "User deleted successfully"
            }

    return app


if __name__ == '__main__':
    app = create_app(__name__)
    app.run()
