import sqlite3
from sqlite3.dbapi2 import Cursor


def create_connection(dbfile):
    try:
        conn = sqlite3.connect(dbfile)
        return conn
    except Exception as e:
        raise Exception(f"Failed to connext to {dbfile}. Error {e}")


def get_users(conn):

    query = "SELECT * FROM users"
    try:
        cursor = conn.cursor()
        data = list(cursor.execute(query))
        return data
    except Exception as e:
        raise Exception("f Failed to extract email and password")


#folosit la metoda POST implementat in Seminar9_api.py
def create_user(conn, user_data):
    query = """insert into users (first_name, last_name, email, password)
     values (?, ?, ?, ?);"""
    try:
        cursor = conn.cursor()
        cursor.execute(query, user_data)
        conn.commit()
    except Exception as e:
        raise Exception("Failed to create user")


def delete_user(conn, id_username):
    query = f"delete from users where id_username ={id_username}"
    cursor = conn.cursor()
    cursor.execute(query, id_username)
    conn.commit()


# def update_user(conn, id_username):
#     query = f"""update id_username users where id_username = '{id_username}'"""
#     cursor = conn.cursor()
#     cursor.execute(query, id_username)
#     conn.commit()

# def get_user_by_username(conn, id_username):
#     query = f"""select username,  password from users where username = '{id_username}'"""
#     cursor = conn.cursor()
#     results = list(cursor.execute(query))
#     return results[0]

# if __name__ == "__main__":
#     from pprint import pprint
#     conn = create_connection("users.db")
#     print(conn)

#     user = get_user_by_username(conn, "username1")
#     pprint(user)

# push_user(conn, details=new_user_details)
# user = get_user_by_username(conn, "newusername_g610_4")
# pprint(user)

#     delete_user(conn, "liviu")
#     users = get_users(conn)
#     pprint(users)

#     new_user_changes = {
#         "password": "lfjkjfbnhjfsihfkhsf",
#         "first_name": "newuserfirstname_updated_2"
#     }

#puteam sa adaugam in forma de dictionar daca functia de sus ne permitea
# new_data = {
#     "first_name": "neeeename",
#     "last_name": "newuestname",
#     "email": "newuser_email.com",
#     "password": "fdkjflksjde420349823rufh"
# }
# create_user(conn, user_data=new_data)

# cursor = conn.cursor()
# query = "select * from users"
# data = cursor.execute(query)
# print(f"Numner of users: { len (data)}")

conn = create_connection(
    "C:\\Users\\ARin\\OneDrive - Romanian-American University (STUD)\\Programarea aplicatiilor Web\\Seminar 1 Github guide\\G610-WebAppProgramming1-AJ\\Seminar 8\\users.db"
)
print(conn)

# insert new users
user1 = ('User 1 Full Name', 'user1@company.com', 'password1234', 'company_id')
user2 = ('User 2 Full Name', 'user2@company.com', 'password12345',
         'company_id')

# user1_id = create_user(conn, user1)
# user2_id = create_user(conn, user2)

# print(user1_id)
# print(user2_id)

# users = get_users(conn)
# print(users)
