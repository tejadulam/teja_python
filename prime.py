num = int(input("enter num: "))
i = 2
rt = int(num**2)
while i <= rt:
    if num%i==0:
        print("not prime")
        break
    i+=1
else:
    print("prime number")
        