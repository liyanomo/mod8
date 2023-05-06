import sqlite3
import datetime

conn  =   sqlite3.connect ('user3.sqlite')
cursor = conn.cursor()
cursor.execute ("CREATE TABLE Students (id int, name Varchar (32), surname Varchar (32), age int, city Varchar (32))")
cursor.execute ("CREATE TABLE Courses (id int, name Varchar (32), time_start Varchar(8), time_end Varchar(8))")
cursor.execute ("CREATE TABLE Student_courses (student_id int, course_id int )")

cursor.executemany("INSERT INTO Students VALUES (?, ?, ?, ?, ?)", [(1, 'Max', 'Brooks', 24, 'Spb'),(2, 'John', 'Stones', 15, 'Spb'), (3, 'Andy', 'Wings', 45, 'Manhester'), (4, 'Kate', 'Brooks', 34, 'Spb')])
cursor.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?)", [(1, 'python', '21.07.21', '21.08.21'),(2, 'java', '13.07.21', '16.08.21')])
cursor.executemany("INSERT INTO Student_courses VALUES (?,?)",[(1,1),(2,1),(3,1),(4,2)])

cursor.execute("SELECT * FROM Students WHERE age >30")
cursor.execute("""SELECT Students.name, Courses.name FROM Students, Courses, Student_Courses WHERE  (Courses.id = 1) AND (Student_Courses.course_id=Courses.id) and (Students.id=Student_Courses.student_id)""")
cursor.execute("""SELECT Students.name, Courses.name, Students.city FROM Students, Courses, Student_Courses WHERE  (Courses.id = 1) AND (Student_Courses.course_id=Courses.id) AND (Students.id=Student_Courses.student_id) AND (Students.city = "Spb" )""")


print (cursor.fetchall())
conn.commit()
conn.close()