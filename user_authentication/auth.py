'''
Module Docstring
This module handles user authentication, including user registration and login.
'''

import hashing
import database

def register_user(username, password):
    '''
    Register a new user with a username and password.
    
    Parameters:
    - username (str): The username for the new user.
    - password (str): The plain-text password for the new user.
    
    Returns:
    - tuple: (bool, str) indicating success/failure and a message explaining the outcome.
    '''
    if database.get_user(username) is not None:
        return False, "Username already exists"

    hashed_password = hashing.hash_password(password)
    if hashed_password is None:
        return False, "An error occurred during password hashing"

    success = database.create_user(username, hashed_password)
    if success:
        return True, "User registered successfully"
    return False, "An error occurred during user registration"

def login_user(username, password):
    '''
    Login a user by their username and password.
    
    Parameters:
    - username (str): The user's username.
    - password (str): The user's password.
    
    Returns:
    - tuple: (bool, str) indicating success/failure and a message explaining the outcome.
    '''
    user_record = database.get_user(username)
    if user_record is None:
        return False, "User not found"

    if hashing.check_password(user_record['hashed_password'], password):
        return True, "Login successful"
    return False, "Invalid username or password"
