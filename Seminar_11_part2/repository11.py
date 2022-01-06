import sqlite3
from sqlite3.dbapi2 import Cursor


def create_connection(dbfile):
    try:
        conn = sqlite3.connect(dbfile)
        return conn
    except Exception as e:
        raise Exception(f"Failed to connext to {dbfile}. Error {e}")


def get_email_and_password(conn, email=None):
    query = f"""select email, password from users where email='{email}'"""
    try:
        cursor = conn.cursor()
        user = list(cursor.execute(query))
        # user can be either [()] or [(a@a.com, lskfjdslkjf)]
        if len(user):
            # user = user[0]
            user = {"email": user[0][0], "password": user[0][1]}
        return user
    except Exception as e:
        raise Exception(
            f"--Failed to extract email and password for user = {email}. Error: {e}."
        )
