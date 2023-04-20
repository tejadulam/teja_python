# -----simple * pogram 

for i in range(1,5):
    print(i*"*")

for i in range(6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

# ------number pattern---
for i in range(5):
    for j in range(1,i+1):
        print(i, end=" ")
    print()

for i in range(6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()
# ------- reversse triangle number pattren----
#  55555, 4444, 333, 22, 1....
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

print()
# 12345, 1234, 123, 12, 1...
for i in range(6,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()

# ------ print pattren 1,23,456,78910 ----
c = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(c,end=" ")
        c+=1
    print()

# -------  1 , 11 , 121, 1231, 12341, 123451..
# for i in range(5):
#     s = ""
#     for j in range(1,i+1):
        