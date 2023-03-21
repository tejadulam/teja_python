#-----Create a list of tuples where each tuple contains a string and an integer. Print out the list
tuple_list = []
n = int(input("enter num: "))
for i in range(n):
    word = input("enter a word: ")
    num = int(input("enter a num: " ))
    tuple_list.append((word,num))
print(tuple_list)
