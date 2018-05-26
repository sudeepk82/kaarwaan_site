#! /home/sudeep/anaconda3/bin/python3.6

import sqlite3
import create_db

connection = sqlite3.connect("schools.sqlite")
cursor = connection.cursor()

def get_stu_id(student_name, school_name):
    no = create_db.select_school(school_name)
    student_id = cursor.execute("""SELECT id FROM """+create_db.schools[no-1]+""" WHERE name=?""", (student_name,)).fetchone()[0]
    return(student_id)

def add_marks(student_id, score, school_name):
    no = create_db.select_school(school_name)
    cursor.execute("""INSERT INTO """+create_db.schools[no-1]+"""_marks (stu_id, marks) VALUES (?, ?)""", (student_id, score))
    connection.commit()
    return(None)


student = str(input("Enter the name of student :\n"))
school = str(input("Enter the name of school :\n"))

st_id = get_stu_id(student, school)

mark = int(input("Enter the marks for student :\n"))

add_marks(st_id, mark, school)

connection.close()