# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 00:55:12 2024

@author: Peter-Emil
"""

import mysql.connector

def get_connection():
    config = {
        'user': 'staffSmart',
        'password': 'pass',
        'host': 'dynamicstaffingdbserver.database.windows.net',
        'database': 'DynamicStaffing_db',
        'raise_on_warnings': True
    }
    try:
        cnx = mysql.connector.connect(**config)
        print("Connection successfully established")
        return cnx
    except mysql.connector.Error as err:
        print(f"Failed to connect: {err}")
        return None
