n = int(input("enter n: "))
c = 0
i = 1
while i<=n:
    if n%i==0:
        c+=1
    i+=1
if c==2:
    print("Prime Number")
else:
    print("Not Prime number")