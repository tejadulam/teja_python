n = int(input("enter n: "))
i = 2
while i <= n//2:
    if n%i==0:
        print("Not Prime")
        break
    i += 1
else:
    print("prime number")