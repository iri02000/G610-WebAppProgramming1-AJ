from os import error
from flask import Flask, request
from flask_cors import CORS
from repository import create_connection, get_users, create_user, update_user, delete_user

app = Flask(__name__)
CORS(app)


@app.route("/users", methods=["GET", "POST", "PUT", "DELETE"])
def users():
    conn = create_connection(
        "C:\\Users\\ARin\\OneDrive - Romanian-American University (STUD)\\Programarea aplicatiilor Web\\Seminar 1 Github guide\\G610-WebAppProgramming1-AJ\\Seminar 8\\users.db"
    )

    # GETmethod: get_users()–retrieve all users available in the databaseas a list of dictionaries with the following keys: username, first_name, last_name, email
    if request.method == "GET":
        conn = create_connection(
            "C:\\Users\\ARin\\OneDrive - Romanian-American University (STUD)\\Programarea aplicatiilor Web\\Seminar 1 Github guide\\G610-WebAppProgramming1-AJ\\Seminar 8\\users.db"
        )
        users = get_users(conn)
        response = request.json
        response = [
            response["id_username"], response["first_name"],
            response["last_name"], response["email"]
        ]
        conn.close()
        return response, 200

    # POSTmethod: create_user() -create a new user and return the id of the newly created user
    if request.method == "POST":  #creeam un user in baza de date     conectat de javascript

        user_data = request.json
        user_data = [
            user_data["first_name"], user_data["last_name"],
            user_data["email"], user_data["password1"]
        ]
        try:
            create_connection(
                "C:\\Users\\ARin\\OneDrive - Romanian-American University (STUD)\\Programarea aplicatiilor Web\\Seminar 1 Github guide\\G610-WebAppProgramming1-AJ\\Seminar 8\\users.db"
            )
            create_user(conn, user_data)
            conn.close()
            return '', 200
        except ValueError as ve:
            return f"--Invalid value provided user. Error message: {ve}.", 400
        except Exception as e:
            error = {"error": f"--Failed to create user. Error message: {e}."}
            return error, 500

        #PUTmethod: update_user(user_id)-update an existing user

        if request.method == "PUT":
            user_details = request.json
            update_user(conn, )


if __name__ == "__main__":
    app.run(port=5006, debug=True)
