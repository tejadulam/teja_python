# -----remove all tuples from a list where the second element of the tuple is even.
list_tup = [("teja",22),("indu",45),("priya",51),("grace",44)]
r = []
for tup in list_tup:
    if tup[1]%2 !=0 :
        r.append(tup)
print(r)
# -----
l = []
n = int(input("enter n: "))
for x in range(n):
    word = input("enter a word: ")
    num = int(input("enter num: "))
    l.append((word,num))
print(l)
r = []
for i in l:
    if i[1]%2!=0:
         r.append(i)
print(r)