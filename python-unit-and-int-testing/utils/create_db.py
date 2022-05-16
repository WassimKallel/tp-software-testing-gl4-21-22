import sqlite3
import os


def create_db(database_filename):
    # connect to SQLite
    con = sqlite3.connect(database_filename)

    # Create a Connection
    cur = con.cursor()

    # Drop users table if already exsist.
    cur.execute("DROP TABLE IF EXISTS users")

    # Create users table  in db_web database
    sql = '''CREATE TABLE "users" (
			"user_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
			"username"	TEXT,
			"fullname"	TEXT
		)'''
    cur.execute(sql)

    # commit changes
    con.commit()

    # close the connection
    con.close()


if __name__ == '__main__':
		database_filename = os.environ.get('DATABASE_FILENAME', 'db_web.db')
		create_db(database_filename)
