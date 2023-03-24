# Given a Python list, write a program to find the value 20 in the list, and if it is present, replace the first occurrence of a value with 200.
# Sample Input: list1 = [5, 10, 15, 20, 25, 50, 20]
# Expected Output:  list1= [5, 10, 15, 200, 25, 50, 20]


list = [5, 10, 15, 20, 25, 50, 20]
list[3] = 200
print(list)