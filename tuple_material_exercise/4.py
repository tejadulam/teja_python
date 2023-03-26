# Write a program to find Dissimilar Elements in Tuples.
# Input:  tuple 1 = (3, 4, 5, 6) , tuple 2 = (5, 7, 4, 10)
# Expected Output: Dissimilar elements = (3, 6, 7, 10)



tuple1 = (3, 4, 5, 6)
tuple2 = (5, 7, 4, 10)
l = []
for x in tuple1:
    if x  in tuple2:
        l.append(x)
print(l)
