'''
Library Management System using OOP concepts:
- Encapsulation
- Inheritance
- File Handling
'''

# Base class (Parent)
class Book:
    def __init__(self, name):
        self.name = name   # encapsulated data

    def get_name(self):
        return self.name


# Child class (Inheritance)
class Library(Book):
    def __init__(self, filename):
        self.filename = filename

    def add_book(self):
        name = input("Enter book name: ")
        book = Book(name)

        file = open(self.filename, "a")
        file.write(book.get_name() + "\n")
        file.close()

        print("Book added!")

    def view_books(self):
        try:
            file = open(self.filename, "r")
            print(file.read())
            file.close()
        except:
            print("No books found!")

    def search_book(self):
        name = input("Enter book name to search: ")
        found = False

        try:
            file = open(self.filename, "r")
            for line in file:
                if name.lower() in line.lower():
                    print("Found:", line)
                    found = True
            file.close()

            if not found:
                print("Book not found!")

        except:
            print("File not found!")

    def borrow_book(self):
        name = input("Enter book to borrow: ")

        try:
            file = open(self.filename, "r")
            books = file.readlines()
            file.close()

            file = open(self.filename, "w")

            found = False
            for b in books:
                if name.lower() not in b.lower():
                    file.write(b)
                else:
                    found = True

            file.close()

            if found:
                print("Book borrowed!")
            else:
                print("Book not available!")

        except:
            print("Error!")

    def return_book(self):
        name = input("Enter book to return: ")

        file = open(self.filename, "a")
        file.write(name + "\n")
        file.close()

        print("Book returned!")


# Main program
lib = Library("books.txt")

while True:
    print("\n1 Add Book\n2 View Books\n3 Search Book\n4 Borrow Book\n5 Return Book\n6 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        lib.add_book()
    elif choice == "2":
        lib.view_books()
    elif choice == "3":
        lib.search_book()
    elif choice == "4":
        lib.borrow_book()
    elif choice == "5":
        lib.return_book()
    elif choice == "6":
        break