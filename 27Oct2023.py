#1.Write a Python program to find the largest number in a list.

mylist = [1,2,7,8,22,99]
print(max(mylist))

#2. Write a Python program to find the smallest number in a list.

mylist = [1,2,7,8,22,99]
print(min(mylist))

# 3. Write a Python program to sum all numbers in a list.

mylist = [1,2,7,8,22,99]
print(sum(mylist))



#4. Write a Python program to multiply all numbers in a list.

#1 method
def mul_list(list):
    # Multiply elements one by one
    product = 1
    for i in list:
        product = product * i
    return product


list1 = [1,2,7,8,22,99]
print(list1)
print("product: ")
print(mul_list(list1))

#2nd method
import  math
def mul_list1(list_1):
    return math.prod(list_1)

list_2 = [1,2,3,4,10]
print(list_2)
print(mul_list1(list_2))




#5. Write a Python program to count the number of strings in a list where the
# string length is 2 or more and the first and last character are the same.

string_list = ['Janhavi','Madam']
len_count = string_list.count('Madam')
print(len_count)