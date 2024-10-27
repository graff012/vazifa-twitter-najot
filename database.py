import mysql.connector

db_name = "TWITTER_FN28"

users_table_sql_scripts = """
    CREATE TABLE IF NOT EXISTS users(
         id BIGINT PRIMARY KEY AUTO_INCREMENT,
         name VARCHAR(34) NOT NULL,
         tel VARCHAR(23),
         username VARCHAR(34) UNIQUE NOT NULL,
         password VARCHAR(34) NOT NULL,
         created_date DATETIME DEFAULT CURRENT_TIMESTAMP
    );
"""

posts_table_sql_scripts = """
    CREATE TABLE IF NOT EXISTS posts(
         id BIGINT PRIMARY KEY AUTO_INCREMENT,
         text VARCHAR(255) NOT NULL,
         created_date DATETIME DEFAULT CURRENT_TIMESTAMP, 
         user_id BIGINT,
         FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
"""

def get_connection():
    try:
        return mysql.connector.connect(
            user="graff",
            password="ubuntu1122",
            host="localhost",
            database=db_name
        )
    except mysql.connector.Error as e:
        print(f"Connection error: {e}")
        return None

def load_db():
    try:
        conn = mysql.connector.connect(
            user="graff",
            password="ubuntu1122",
            host="localhost"
        )

        cur = conn.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        conn.commit()

        cur.close()
        conn.close()

        conn = get_connection()
        if conn is None:
            return

        cur = conn.cursor()

        cur.execute(users_table_sql_scripts)
        cur.execute(posts_table_sql_scripts)

        conn.commit()

    except mysql.connector.Error as e:
        print(f"Database error: {e}")
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def load_data():
    users_insert_scripts = """
        INSERT INTO users (name, tel, username, password) VALUES 
        ('Alice Johnson', '123-456-7890', 'aliej', 'password1'),
        ('Bob Smith', '098-765-4321', 'bobsmith', 'password2'),
        ('Charlie Brown', '555-555-5555', 'charlieb', 'password3'),
        ('Diana Prince', '123-321-1234', 'dianap', 'password4'),
        ('Ethan Hunt', '654-321-9870', 'ethanh', 'password5'),
        ('Fiona Gallagher', '111-222-3333', 'fionag', 'password6'),
        ('George Clooney', '222-333-4444', 'georgec', 'password7'),
        ('Hannah Baker', '444-555-6666', 'hannahb', 'password8'),
        ('Ian Malcolm', '777-888-9999', 'ianm', 'password9'),
        ('Julia Roberts', '000-111-2222', 'juliar', 'password10');
    """

    posts_insert_scripts = """
        INSERT INTO posts (text, user_id) VALUES 
        ('This is Alices first post!', 1),
        ('Bob Smith shares his thoughts on technology.', 2),
        ('Charlie Brown loves programming in Python.', 3),
        ('Diana Prince just returned from her adventure.', 4),
        ('Ethan Hunt completed another mission successfully.', 5),
        ('Fiona Gallagher shares her favorite recipes.', 6),
        ('George Clooney is filming a new movie.', 7),
        ('Hannah Baker has a lot to say about mental health.', 8),
        ('Ian Malcolm discusses the ethics of cloning.', 9),
        ('Julia Roberts expresses her love for acting.', 10);
    """

    con = get_connection()
    if con is None:
        return

    try:
        cur = con.cursor()

        cur.execute("DELETE FROM posts;")
        cur.execute("DELETE FROM users;")

        cur.execute("ALTER TABLE users AUTO_INCREMENT = 1;")

        cur.execute(users_insert_scripts)
        con.commit()
        print("Users inserted successfully.")

        cur.execute(posts_insert_scripts)
        con.commit()
        print("Posts inserted successfully.")

    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
    finally:
        if 'cur' in locals():
            cur.close()
        con.close()


def executive_sql_get(script, params=None):
    con = get_connection()
    if con is None:
        return []

    try:
        cur = con.cursor()
        cur.execute(script, params)
        data = cur.fetchall()
        return data

    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")
        return []
    finally:
        cur.close()
        con.close()

def executive_sql_commit(script, params=None):
    con = get_connection()
    if con is None:
        return False

    try:
        cur = con.cursor()
        cur.execute(script, params)
        con.commit()
        return True

    except mysql.connector.Error as e:
        print(f"Error executing commit: {e}")
        return False
    finally:
        cur.close()
        con.close()

if __name__ == "__main__":
    load_db()
    load_data()
