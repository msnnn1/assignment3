'''
Program to perform operations on list of integers and save results to file.
'''

file = open("result.txt", "a")

while True:
    nums = input("Enter numbers separated by space: ")
    numbers = nums.split()

    numbers = [int(n) for n in numbers]

    add = sum(numbers)

    sub = numbers[0]
    for i in numbers[1:]:
        sub = sub - i

    mul = 1
    for i in numbers:
        mul = mul * i

    div = numbers[0]
    for i in numbers[1:]:
        if i != 0:
            div = div / i

    result = "Add=" + str(add) + " Sub=" + str(sub) + " Mul=" + str(mul) + " Div=" + str(div) + "\n"

    file.write(result)

    choice = input("Do you want to continue? (yes/no): ")
    if choice == "no":
        break

file.close()

print("\nSaved Results:")
file = open("result.txt", "r")
print(file.read())
file.close()