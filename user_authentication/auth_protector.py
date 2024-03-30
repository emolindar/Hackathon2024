'''
Module Docstring
This module provides a decorator function to protect routes that require user authentication.
'''

from functools import wraps
from flask import session, redirect, url_for

def login_required(f):
    '''
    Decorator to require login for certain functions.
    Redirects to the login page if the user is not logged in.
    
    Usage:
    @login_required
    def some_protected_function():
        pass
    '''
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session or not session['logged_in']:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
