# Write a program to add 7000 after 6000 in the following list.
# Sample Input:  list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected Output:  list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]


list = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list[2][2].insert(2,7000)
print(list)
