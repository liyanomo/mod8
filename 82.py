from peewee import *

conn = SqliteDatabase ('users03.sqlite') 

class BaseModel(Model):
    class Meta:
        database = conn

class Students(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    surname = CharField()
    age = IntegerField()
    city = CharField()

class Courses (BaseModel):
	id = PrimaryKeyField()
	name = CharField()
	time_start = CharField()
	time_end = CharField()

class Student_courses(BaseModel):
	student_id = ForeignKeyField(Students, to_field = "id")
	course_id = ForeignKeyField(Courses, to_field = "id")
def create_tbls():
    Students.create_table()
    Courses.create_table()
    Student_courses.create_table()

    student = Students(name = "Max", surname = "Brooks", age=24 , city = "Spb")
    student.save()
    student = Students(name = "John", surname = "Stones", age=15 , city = "Spb")
    student.save()
    student = Students(name = "Andy", surname = "Wings", age=45 , city = "Manhester")
    student.save()
    student = Students(name = "Kate", surname = "Brooks", age=34 , city = "Spb")
    student.save()

    courses = Courses(id = 1, name = "python", time_start = "21.07.21" , time_end = "21.08.21" )
    courses.save ()
    courses = Courses(id = 2, name = "java", time_start = "13.07.21" , time_end = "16.08.21" )
    courses.save ()

    st_courses = Student_courses (student_id = 1,course_id = 1)
    st_courses.save()
    st_courses = Student_courses (student_id = 2,course_id = 1)
    st_courses.save()
    st_courses = Student_courses (student_id = 3,course_id = 1)
    st_courses.save()
    st_courses = Student_courses (student_id = 4,course_id = 2)
    st_courses.save()

#create_tbls()
#for student in Students.select().where(Students.age > 30):
#	print(student.name)


for student in Students.select().join(Student_courses).where ((Student_courses.course_id == 1) & (Students.id == Student_courses.student_id)):
    print(student.name, 'python')


#for student in Students.select().join(Student_courses).where ((Students.city == 'Spb') & (Student_courses.course_id == 1) & (Students.id == Student_courses.student_id)):
#     print(student.name, 'python', student.city)

conn.close()