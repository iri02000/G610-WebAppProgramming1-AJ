from flask import Flask, request
from flask_cors import CORS
from repo import create_connection, get_users, create_user, delete_user

app = Flask(__name__)

CORS(app)

database = "C:\\Users\\ARin\\OneDrive - Romanian-American University (STUD)\\Programarea aplicatiilor Web\\Seminar 1 Github guide\\G610-WebAppProgramming1-AJ\\Seminar 8\\users.db"


@app.route("/users", methods=["GET", "POST", "DELETE"])
def users():
    conn = create_connection(database)

    # GETmethod: get_users()–retrieve all users available in the databaseas a list of dictionaries with the following keys: username, first_name, last_name, email

    # if request.method == "GET":
    #     users = get_users(conn)
    #     body = request.json
    #     response = [
    #         response["id_username"], response["first_name"],
    #         response["last_name"], response["email"]
    #     ]
    #     conn.close()
    #     return response, 200

    # # POSTmethod: create_user() -create a new user and return the id of the newly created user

    if request.method == "POST":  #creeam un user in baza de date     conectat de javascript
        user_data = request.json  # user_details e de tip dictionar pt ca folosim jason, ia date din http
        # aici am transformat din dictionar in lista pt ca functia create_user introduce datele in forma de lista

        details = [
            user_data.get("firstname", None),
            user_data.get("lastname", None),
            user_data.get("email", None),
            user_data.get("password", None)
        ]
        try:
            create_connection(database)
            create_user(conn, details)
            conn.close()
            return '', 200
        except ValueError as ve:
            return f"--Invalid value provided user. Error message: {ve}.", 400
        except Exception as e:
            error = {"error": f"--Failed to create user. Error message: {e}."}
            return error, 500


if __name__ == "__main__":
    app.run(port=5006, debug=True)
