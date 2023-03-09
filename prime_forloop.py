num = int(input("enter num: "))
rt = int(num**.5)
for i in range(2,rt+1):
    if num%i==0:
        print("not prime")
        break
else:
    print("prime")
