# students = []


# class Student:

#    school_name = "Springfield Elementary"

#    def add_student(self, name, student_id=332):
#    def __init__(self, name, student_id=332):
#        self.name = name
#        self.student_id = student_id
#        students.append(self)
#        student = {"name": name, "student_id": student_id}
#        students.append(student)
#    pass
#        self.add_student()
#    def __str__(self):
#        return "Student " + self.name

#    def get_name_capitalize(self):
#        return self.name.capitalize()

#    def get_school_name(self):
#        return self.school_name


# mark = Student("Mark")
# print(mark)

# student = Student()
# student.add_student("Mark")

# print(students)

# new_student = Student()

# print(new_student)

# print(Student.school_name)

# class HighSchoolStudent(Student):

#    school_name = "Springfield High School"

#    def get_school_name(self):
#        return "This is a High School student"

#    def get_name_capitalize(self):
#        original_value = super().get_name_capitalize()
#        return  original_value + "-HS"


# james = HighSchoolStudent("james")
# print(james.get_school_name())
# print(james.get_name_capitalize())


students = []


class Student:

	school_name = "Springfield Elementary"

	def __init__(self, name, student_id=332):
		self.name = name
		self.student_id = student_id
		students.append(self)

	def __str__(self):
		return "Student " + self.name

	def get_name_capitalize(self):
		return self.name.capitalize()

	def get_school_name(self):
		return self.school_name


class HighSchoolStudent(Student):

	school_name = "Springfield High School"

	def get_school_name(self):
		return "This is a High School student"

	def get_name_capitalize(self):
		original_value = super().get_name_capitalize()
		return original_value + "-HS"


james = HighSchoolStudent("james")
print(james.get_name_capitalize())