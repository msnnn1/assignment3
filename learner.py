'''
This program creates a Learner class and shows details.
'''

class Learner:
    def __init__(self):
        self.roll_no = ""
        self.full_name = ""
        self.address = ""
        self.enrollment_year = ""
        self.program = ""
        self.group = ""

learner = Learner()

learner.roll_no = input("Enter roll number: ")
learner.full_name = input("Enter full name: ")
learner.address = input("Enter address: ")
learner.enrollment_year = input("Enter enrollment year: ")
learner.program = input("Enter program: ")
learner.group = input("Enter group: ")

print("Learner Details")
print("Roll No:", learner.roll_no)
print("Full Name:", learner.full_name)
print("Address:", learner.address)
print("Enrollment Year:", learner.enrollment_year)
print("Program:", learner.program)
print("Group:", learner.group)