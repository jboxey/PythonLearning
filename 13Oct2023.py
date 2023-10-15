# Task 1: Write a Python program to calculate the area of a circle given its radius using the formula
# area=π×r^2 ( Take pie as 3.14)

radius = 7
a =2
area_of_circle = 3.14*(radius)**(a)
print(area_of_circle)


# Task 2: Create a program that takes two numbers as input and prints whether the
# first number is greater than, less than, or equal to the second number.
# Use the ternary operator to find the maximum of three numbers entered by the user.

number_1 = input("Enter number 1 \n")
number_2 = input("Enter number 2 \n")
number_3 = input("Enter number 3 \n")

# Ternary Operator
max_val = number_1 if(number_1 > number_2 and number_1>number_3) else(number_2 if number_2 >number_3 else number_3)
print(max_val)

print(number_1>=number_2)
print(number_1>=number_2)
print(number_1<=number_2)


#Task 3: Develop a Python script that calculates the square and cube of a given number.
number = int(input("Enter a number \n"))
square = number ** 2
print(square)
cube =pow(number, 3)
print(cube)



