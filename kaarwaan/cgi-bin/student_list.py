#! /home/sudeep/anaconda3/bin/python3.6

import sqlite3
import create_db

connection = sqlite3.connect("schools.sqlite")
cursor = connection.cursor()


school = str(input("Enter the name of school : \n"))

school_id = create_db.select_school(school)

student_list = [row [0] for row in cursor.execute("""SELECT name from """+create_db.schools[school_id-1]).fetchall()]

for i in range(len(student_list)):
    print(student_list[i])

