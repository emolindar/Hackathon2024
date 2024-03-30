'''
Module Docstring
This module provides functionalities for interacting with the user authentication database,
including creating users and retrieving user data securely.
'''

import sqlite3

DATABASE_PATH = 'path/to/your/database.db'

def create_connection():
    '''
    Create and return a database connection.
    
    Returns:
    - connection: A SQLite connection object.
    '''
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def create_user(username, hashed_password):
    '''
    Create a new user with a username and hashed password.
    
    Parameters:
    - username (str): The username of the new user.
    - hashed_password (bytes): The hashed password of the new user.
    
    Returns:
    - bool: True if user was created successfully, False otherwise.
    '''
    conn = create_connection()
    if conn is not None:
        try:
            with conn:
                conn.execute("INSERT INTO users (username, hashed_password) VALUES (?, ?)",
                             (username, hashed_password))
            return True
        except sqlite3.IntegrityError:
            print("Username already exists.")
            return False
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
        finally:
            conn.close()
    return False

def get_user(username):
    '''
    Retrieve a user by username.
    
    Parameters:
    - username (str): The username of the user to retrieve.
    
    Returns:
    - dict: A dictionary containing the user's data, or None if the user was not found.
    '''
    conn = create_connection()
    if conn is not None:
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("SELECT username, hashed_password FROM users WHERE username = ?",
                            (username,))
                row = cur.fetchone()
                if row:
                    return {'username': row[0], 'hashed_password': row[1]}
                return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            conn.close()
    return None
