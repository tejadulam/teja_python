#  abversion names in short cut 

n = input("enter name: ")
n = n.split()
for i in range(len(n)-1):
    print(f"{n[i][0]}.",end=' ')
print(n[-1])