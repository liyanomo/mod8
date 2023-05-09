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
    #Students.create_table()
    #Courses.create_table()
    #Student_courses.create_table()

    Students = [ { 'id': 1, 'name':'Max', 'surname':'Brooks', 'age': 24, 'city':'Spb'},
{'id': 2, 'name':'John', 'surname':'Stones', 'age': 15, 'city':'Spb'},
{'id': 3, 'name':'Andy', 'surname':'Wings', 'age': 45, 'city':'Manchester'},
{'id': 4, 'name':'Kate', 'surname':'Brooks', 'age': 34, 'city':'Spb'}
]
    Students.insert_many(Students).execute()
    Courses = [
{'id':1, 'course_name':'python', 'time_start':'21.07.21', 'time_end':'21.08.21'},
{'id':2, 'course_name':'java', 'time_start':'13.07.21', 'time_end':'16.08.21'}
]
    Course.insert_many(Courses).execute()
    Student_courses = [
{ 'student_id': s[0], 'course_id': c[0]},
{ 'student_id': s[1], 'course_id': c[0]},
{ 'student_id': s[2], 'course_id': c[0]},
{ 'student_id': s[3], 'course_id': c[1]}
]
    Student_course.insert_many(Student_courses).execute() 

#create_tbls()
for student in Students.select().where(Students.age > 30):
	print(student.name)

print ('__________')


for student in Students.select().join(Student_courses).where ((Student_courses.course_id == 1) & (Students.id == Student_courses.student_id)):
    print(student.name, 'python')

print ('_________')


for student in Students.select().join(Student_courses).where ((Students.city == 'Spb') & (Student_courses.course_id == 1) & (Students.id == Student_courses.student_id)):
     print(student.name, 'python', student.city)

conn.close()