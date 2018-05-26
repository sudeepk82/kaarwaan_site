#! /home/sudeep/anaconda3/bin/python3.6

import sqlite3

def get_names():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    results = cursor.execute("""SELECT name from students""")

    names = [row[0] for row in results.fetchall()]
    return(names)

def view_names():
    for i in range(len(get_names)):
        
