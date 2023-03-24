# Write a program to print the list of numbers which are greater than the average of numbers in the following list.
# Sample Input: list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
# Expected Output: [9, 13, 12, 7]

list = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
s = 0
for x in list:
    s+=x
    avg = s/len(list)
print(avg)
l = []
for x in list:
    if x >= avg:
        l.append(x)
print(l)