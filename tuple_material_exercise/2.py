# Write a program to count the number of even and odd numbers from a tuple of numbers.
# Input : tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output:
# Number of even numbers: 5  Number of odd numbers: 4

tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for x in tuple:
    if x % 2==0:
        even+=1
    else:
        odd+=1
print("Number of even numbers:",even)
print("Number of odd numbers:",odd)


