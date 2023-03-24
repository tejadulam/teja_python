# Write a Python program to get the difference between the two lists.
# Sample Input:  list1 = [1, 2, 3, 4] , list2 = [1, 2]
# Expected Output: [3,4]

list1 = [1, 2, 3, 4]
list2 = [1, 2]
l = []
for x in list1:
    if x not in list2:
        l.append(x)
print(l)
