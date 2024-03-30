'''
Module Docstring
This module provides functionalities for hashing and verifying passwords securely using bcrypt.
'''

import bcrypt

def hash_password(plain_text_password):
    '''
    Hash a password for storing.
    
    Parameters:
    - plain_text_password (str): The password in plain text to be hashed.
    
    Returns:
    - bytes: The hashed password, or None if hashing failed.
    '''
    try:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
        return hashed
    except ValueError as e:
        print(f"Error hashing password: {e}")
        return None

def check_password(hashed_password, user_password):
    '''
    Verify a stored password against one provided by user.
    
    Parameters:
    - hashed_password (bytes): The hashed password stored in the database.
    - user_password (str): The password provided by the user, to compare against the stored
    hashed password.
    
    Returns:
    - bool: True if the password provided by the user matches the hashed password, False otherwise.
    '''
    try:
        return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)
    except ValueError as e:
        print(f"Error verifying password: {e}")
        return False
