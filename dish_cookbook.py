'''
This program stores dishes in a cookbook.
'''

class Dish:
    def __init__(self, id, name, ingredients, instructions):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions


class Cookbook:
    def __init__(self):
        self.list = []

    def add(self, dish):
        self.list.append(dish)

    def show(self):
        for d in self.list:
            print(d.id, d.name, d.ingredients, d.instructions)


c = Cookbook()

id = input("Enter dish id: ")
name = input("Enter dish name: ")
ingredients = input("Enter ingredients: ")
instructions = input("Enter instructions: ")

d = Dish(id, name, ingredients, instructions)

c.add(d)
c.show()