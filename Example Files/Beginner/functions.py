students = []


def get_students_titlecase():
	students_titlecase = []
	for student in students:
		students_titlecase.append(student["name"].title())
#		students_titlecase = student["name"].title()
	return students_titlecase


def print_students_titlecase():
	students_titlecase = get_students_titlecase()
	print(students_titlecase)


def add_student(name, student_id = 332):
	student = {"name": name, "student_id": student_id}
	students.append(student)


def save_file(student):
	try:
		f = open("students.txt", "a")
		f.write(student + "\n")
		f.close()
	except Exception:
		print("Could not save file")


def read_file():
	try:
		f = open("students.txt", "r")
		for student in f.readlines():
			add_student(student)
		f.close()
	except Exception:
		print("Could not read file")

#def var_args(name, **kwargs):
#	print(name)
#	print(kwargs["description"], kwargs["feedback"])

#student_list = get_students_titlecase()

#add_student(name = "Mark", student_id = 15)

#var_args("Mark", description = "Loves Python", feedback = None, pluralsight_subscriber = True)

read_file()
print_students_titlecase()

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

add_student(student_name, student_id)
#print_students_titlecase()
save_file(student_name)