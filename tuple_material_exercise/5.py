# Write a program for addition of tuples.
# Input: tuple1 = (10, 4, 5) tuple2 = (2, 5, 18)
# Expected Output: new_tuple = (12, 9, 23)

tuple1 = (10, 4, 5)
tuple2 = (2, 5, 18)
list1 = list(tuple1)
list2 = list(tuple2)
s = list1[0]+list2[0], list1[1]+list2[1], list1[2]+list2[2]
print(s)