# Write a program to add member(s) in a set.
# Input: set1 = {'Blue'} set2 = {'Green', 'Yellow'}
# Expected Output: {'Blue', 'Green', 'Yellow'}

set1 = {'Blue'}
set2 = {'Green', 'Yellow'}
set1.update(set2)
print(set1)