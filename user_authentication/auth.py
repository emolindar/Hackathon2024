'''
module docstring'''
import hashing
import database

def register_user(username, password):
    '''
    function docstring'''
    if database.get_user(username) is not None:
        return False, "Username already exists"

    hashed_password = hashing.hash_password(password)

    success = database.create_user(username, hashed_password)
    if success:
        return True, "User registered successfully"
    return False, "An error occurred during user registration"

def login_user(username, password):
    '''
    function docstring'''
    user_record = database.get_user(username)
    if user_record is None:
        return False, "User not found"

    if hashing.check_password(user_record['hashed_password'], password):
        return True, "Login successful"
    return False, "Invalid username or password"
