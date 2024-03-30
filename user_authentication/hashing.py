'''
module docstring'''
import bcrypt

def hash_password(plain_text_password):
    '''
    function docstring'''
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
    return hashed

def check_password(hashed_password, user_password):
    '''
    function docstring'''
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)
