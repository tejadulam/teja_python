# Write a program to know how many times an element occurred in the list.
# Sample Input:  list1 = [5, 10, 15, 20, 25, 50, 20]
# element = 20 # Expected Output:2


list = [5, 10, 15, 20, 25, 50, 20]
s = list.count(20)
print(s)


l = []
element = int(input("enter num: "))
for x in range(7):
    num = int(input("enter n: "))
    l.append(num)
print(l)
cou = l.count(element)
print(cou)
    