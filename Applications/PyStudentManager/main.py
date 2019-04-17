"""
Simple console app called "PyStudentManager" made through Pluralsight Course.
Application can add and display student names, last names and student IDs.
"""

from hs_student import *

james = HighSchoolStudent("james", "bond")
print(james.get_name_capitalize())