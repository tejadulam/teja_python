# Python program to remove duplicates from a list.
# Sample Input: list1 = [10,20,30,20,10,50,60,40,80,50,40]
# Expected Output : [10, 20, 30, 50, 60, 40, 80]

list = [10,20,30,20,10,50,60,40,80,50,40]
l = []
for x in list:
    if x not in l:
        l.append(x)
print(l)
    
list1 = [10,20,30,20,10,50,60,40,80,50,40]
print(list(set(list1)))