# Write a Python program to find common items from two lists.
# Sample Input
# color1 = ["Red", "Green", "Orange", "White"]
# color2 = ["Black", "Green", "White", "Pink"]
# Expected Output :['Green', 'White']


color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
l = []
for x in color1:
    if x in color2:
        l.append(x)
print(l)
        
