"""
This script is designed to test the functionality of the password_db.py module,
specifically focusing on creating and retrieving user records in the MySQL database.
It uses bcrypt for password hashing to simulate the password handling process.
"""

import bcrypt
from password_db import create_user, get_user

def test_create_and_get_user():
    """
    Tests the creation of a user and retrieval of the same user from the database.
    It performs the following operations:
    1. Hashes a password using bcrypt.
    2. Attempts to create a user with a username and the hashed password.
    3. Attempts to retrieve the newly created user.
    4. Verifies that the hashed password retrieved matches the original password.
    """
    # Define test credentials
    username = "test_user"
    password = "securepassword"

    # Hash the password to simulate storing a hashed password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Attempt to create the user in the database
    created = create_user(username, hashed_password)
    print(f"User Creation: {'Success' if created else 'Failure'}")

    # Attempt to retrieve the user from the database
    user = get_user(username)
    if user:
        print(f"User /Retrieved: Username: {user['username']}",
              "Hashed Password:/s{user['hashed_password']}")
    else:
        print("User not found.")

    # Verify that the retrieved hashed password matches the original password
    if user and bcrypt.checkpw(password.encode('utf-8'), user['hashed_password']):
        print("Password verification successful.")
    else:
        print("Password verification failed.")

if __name__ == "__main__":
    # Run the test function
    test_create_and_get_user()
