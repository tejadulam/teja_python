# ----Write a program to iterate over a list of tuples and print out the first element of each tuple.
list_tuple = []
n = int(input("enter the num of tuples: "))
for i in range(n):
    word = input("enter a word: ")
    num = int(input("enter a num: "))
    list_tuple.append((word,num))
print(list_tuple)
for x in list_tuple:
     print(x[0])
