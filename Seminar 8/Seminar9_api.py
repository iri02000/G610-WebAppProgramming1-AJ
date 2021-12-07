from flask import Flask, request

from repository import create_connection, get_users, create_user, update_user, delete_user

app = Flask(__name__)


@app.route("/api/v1/users", methods=["GET", "POST", "PUT", "DELETE"])
def users():
    conn = create_connection(
        "C:\\Users\\ARin\\OneDrive - Romanian-American University (STUD)\\Programarea aplicatiilor Web\\Seminar 1 Github guide\\G610-WebAppProgramming1-AJ\\Seminar 8\\users.db"
    )

    # GETmethod: get_users()–retrieve all users available in the databaseas a list of dictionaries with the following keys: username, first_name, last_name, email
    if request.method == "GET":
        users = get_users(conn)
        response = request.json
        response = [
            response["id_username"], response["first_name"],
            response["last_name"], response["email"]
        ]
        conn.close()
        return response, 200

    # POSTmethod: create_user() -create a new user and return the id of the newly created user
    if request.method == "POST":
        user_data = request.json
        user_data = [
            user_data["id_username"], user_data["first_name"],
            user_data["last_name"], user_data["email"], user_data["password"],
            user_data["created_at"], user_data["last_updated"],
            user_data["last_signed"]
        ]
        create_user(conn, user_data)
        conn.close()
        return '', 200

        #PUTmethod: update_user(user_id)-update an existing user

        if request.method == "PUT":
            user_details = request.json
            update_user(conn, )


if __name__ == "__main__":
    app.run(port=5006, debug=True)
