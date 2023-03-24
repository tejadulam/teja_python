# Write a program to find difference between sum of even indexed and odd indexed numbers in a list of numbers. [Note:- Consider 0th index as even indexed]
# Sample Input:  list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
# Expected Output:  -10

list = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
even = list[0::2]
even_s= sum(even)
odd = list[1::2]
odd_s = sum(odd)
print(even_s - odd_s)

even_sum = sum(list[0::2])
odd_sum = sum(list[1::2])
print(even_sum - odd_sum)
