'''
This program copies content from one file to another.
'''

source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

try:
    file1 = open(source, "r")
    data = file1.read()
    file1.close()

    file2 = open(destination, "x")
    file2.write(data)
    file2.close()

    print("File copied successfully!")

except FileNotFoundError:
    print("Source file not found!")

except FileExistsError:
    print("Destination file already exists!")