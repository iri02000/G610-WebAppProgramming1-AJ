import sqlite3
from sqlite3.dbapi2 import Cursor


def create_connection(dbfile):
    conn = sqlite3.connect(dbfile)
    return conn


def get_users(conn):
    query = "SELECT * FROM users"
    cursor = conn.cursor()
    data = cursor.execute(query)
    return data


# def get_user_by_username(conn, id_username):
#     query = f"""select username,  password from users where username = '{id_username}'"""
#     cursor = conn.cursor()
#     results = list(cursor.execute(query))
#     return results[0]


#folosit la metoda POST implementat in Seminar9_api.py
def create_user(conn, user_data):
    query = """insert into users (first_name, last_name, email, password)
     values (?, ?, ?, ?);"""
    cursor = conn.cursor()
    cursor.execute(query, user_data)
    conn.commit()


def delete_user(conn, id_username):
    query = f"delete from users where id_username ={id_username}"
    cursor = conn.curs
    cursor.execute(query, id_username)
    conn.commit()


def update_user(conn, id_username):
    query = f"""update id_username users where id_username = '{id_username}'"""
    cursor = conn.cursor()
    cursor.execute(query, id_username)
    conn.commit()


# if __name__ == "__main__":
#     from pprint import pprint
#     conn = create_connection("users.db")
#     print(conn)

#     user = get_user_by_username(conn, "username1")
#     pprint(user)

# new_user_details = {
#     "username": "newusername_g610_4",
#     "first_name": "newuserfirstname",
#     "last_name": "newuserlastname",
#     "email": "newuser_g610_4@email.com",
#     "password": "fdkjflksjdf48375420349823rufh"
# }
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

conn = create_connection(
    "C:\\Users\\ARin\\OneDrive - Romanian-American University (STUD)\\Programarea aplicatiilor Web\\Seminar 1 Github guide\\G610-WebAppProgramming1-AJ\\Seminar 8\\users.db"
)
print(conn)

users = get_users(conn)
print(users)

# cursor = conn.cursor()
# query = "select * from users"
# data = cursor.execute(query)
# print(f"Numner of users: { len (data)}")