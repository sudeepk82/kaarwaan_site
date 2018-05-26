#! /home/sudeep/anaconda3/bin/python3.6

import sqlite3

def create_tables():
    connection = sqlite3.connect("schools.sqlite")
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE lny(
                        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                        name TEXT NOT NULL,
                        dob DATE NOT NULL DEFAULT '1997-10-20')
                    """)

    cursor.execute("""CREATE TABLE lny_marks(
                        stu_id INTEGER NOT NULL,
                        marks INTEGER,
                        FOREIGN KEY (stu_id) REFERENCES lny)
                    """)

    cursor.execute("""CREATE TABLE gokalpur(
                        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                        name TEXT NOT NULL,
                        dob DATE NOT NULL DEFAULT '1997-10-20')
                    """)

    cursor.execute("""CREATE TABLE gokalpur_marks(
                        stu_id INTEGER NOT NULL,
                        marks INTEGER,
                        FOREIGN KEY (stu_id) REFERENCES gokalpur)
                    """)

    cursor.execute("""CREATE TABLE lake(
                        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                        name TEXT NOT NULL,
                        dob DATE NOT NULL DEFAULT '1997-10-20')
                    """)

    cursor.execute("""CREATE TABLE lake_marks(
                        stu_id INTEGER NOT NULL,
                        marks INTEGER,
                        FOREIGN KEY (stu_id) REFERENCES lake)
                    """)

    cursor.execute("""CREATE TABLE mastana(
                        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                        name TEXT NOT NULL,
                        dob DATE NOT NULL DEFAULT '1997-10-20')
                    """)

    cursor.execute("""CREATE TABLE mastana_marks(
                        stu_id INTEGER NOT NULL,
                        marks INTEGER,
                        FOREIGN KEY (stu_id) REFERENCES mastana)
                    """)

    connection.commit()
    connection.close()

    return(None)

schools = ["lny", "gokalpur", "lake", "mastana"]

def select_school(data):
    for i in range(len(schools)):
        if schools[i] in data:
            check = i + 1
            break
        else:
            check = 0
    return(check)

