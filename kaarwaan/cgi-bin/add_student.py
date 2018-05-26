#! /home/sudeep/anaconda3/bin/python3.6

import sqlite3
import glob
import create_db

files = glob.glob("*.sqlite")

if "schools.sqlite" not in files:
    create_db.create_tables()

def get_stu_id(student_name, school_name):
    no = create_db.select_school(school_name)
    student_id = cursor.execute("""SELECT id from """+create_db.schools[no-1]+""" WHERE name=?""", (student_name,)).fetchone()[0]
    return(student_id)

def add_marks(student_id, score, school_name):
    no = create_db.select_school(school_name)
    cursor.execute("""INSERT INTO """+create_db.schools[no-1]+"""_marks (stu_id, marks) VALUES (?, ?)""", (student_id, score))
    connection.commit()
    return(None)

school = str(input("Please Enter the school name \n"))

school_id = create_db.select_school(school)

stu_name = str(input("Please Enter student's name : \n"))
stu_dob = str(input("Enter student's Date of Birth (yyyy-mm-dd) : \n"))

connection = sqlite3.connect("schools.sqlite")
cursor = connection.cursor()

cursor.execute("""INSERT INTO """+create_db.schools[school_id-1]+""" (name, dob) VALUES (?, ?)""", (stu_name, stu_dob))
connection.commit()

response = str(input("Do you want to enter marks for student??? (yes/no) \n"))

while response == "yes":
    mark = int(input("Enter the marks for student : "))
    add_marks(get_stu_id(stu_name, school), mark, school)
    response = str(input("Do you want to enter more marks???"))

connection.close()