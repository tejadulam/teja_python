# ----create a list of tuples where each tuple contains a string and the length of the string.


l = []
n = int(input("enter np of tuples:"))
for x in range(n):    
    word = input("enter word: ")
    l.append((word,len(word)))
print(l)

