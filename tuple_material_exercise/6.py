# pogram to remove duplicates

s = (2,3,4,5,3,2,6,7,8,5)
v = set(s)
print(tuple(v))

s = (2,3,4,5,3,2,6,7,8,5)
l = []
for  x in s:
    if x not in l:
        l.append(x)
print(tuple(l))