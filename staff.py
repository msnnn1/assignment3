'''
This program stores staff details in a file.
'''

file = open("staff.csv", "a")

try:
    id = input("Enter ID: ")
    name = input("Enter name: ")
    address = input("Enter address: ")
    phone = input("Enter phone: ")
    marital = input("Enter marital status: ")
    dependents = input("Enter dependents: ")
    salary = input("Enter salary: ")

    data = id + "," + name + "," + address + "," + phone + "," + marital + "," + dependents + "," + salary + "\n"

    file.write(data)

    file.close()

    print("\nStaff List:")
    file = open("staff.csv", "r")
    print(file.read())
    file.close()

except:
    print("Error occurred!")