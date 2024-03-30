'''
module docstring this is a placeholder for the database'''
def create_user(username, hashed_password):
    '''
    function docstring'''
    return True

def get_user(username):
    '''
    function docstring'''
    user_record = {
        'username': username,
        'hashed_password': b'somehashedpassword'
    }
    return user_record
