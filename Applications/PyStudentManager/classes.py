students = []


# Defining student class!
class Student:

	school_name = "Springfield Elementary"

	def __init__(self, name, last_name, student_id=332):
		self.name = name
		self.last_name = last_name
		self.student_id = student_id
		students.append(self)

	def __str__(self):
		return "Student " + self.name + self.last_name

	def get_name_capitalize(self):
		return self.name.capitalize() + self.last_name.capitalize()

	def get_school_name(self):
		return self.school_name


# Using heritance of student class
class HighSchoolStudent(Student):

	school_name = "Springfield High School"

	def get_school_name(self):
		return "This is a High School student"

	def get_name_capitalize(self):
		original_value = super().get_name_capitalize()
		return original_value + "-HS"


james = HighSchoolStudent("james", "boeing")
print(james.get_name_capitalize())