#! /home/sudeep/anaconda3/bin/python3.6

import sqlite3
import create_db

connection = sqlite3.connect("schools.sqlite")
cursor = connection.cursor()

school = str(input("Enter school name : \n"))
student = str(input("Enter student's name : \n"))


def get_stu_id(student_name, school_name):
    no = create_db.select_school(school_name)
    student_id = cursor.execute("""SELECT id from """+create_db.schools[no-1]+""" WHERE name=?""", (student_name,)).fetchone()[0]
    return(student_id)

def get_marks(stu_id, school_name):
    no = create_db.select_school(school_name)
    marks = [row[0] for row in cursor.execute("""SELECT marks from """+create_db.schools[no-1]+"""_marks WHERE stu_id=?""", (stu_id,)).fetchall()]
    return(marks)

marks_list = get_marks((get_stu_id(student, school)), school)

print(school)
print(student)
for i in range(len(marks_list)):
    print(marks_list[i])
