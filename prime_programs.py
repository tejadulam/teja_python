
#  How to find factors and their count 
n = int(input("Enter num: "))
i = 1
count = 0
while i <= n:
    if n % i == 0:
        print(i)
        count += 1
    i += 1
print("Total Factors count is",count)



# ------ to check whether the given number is prime or not ----

# ----- complexity is o(n)
''' first we are taking that num as a user input 
then take i and  c variables ... 
set i value as 1 because 1 is the smallest possible factor for any number...
checking that i is less than for equal to number.... 
then divide the num with i if it is equal to 0...then increment the count value
else increment i value ....
here we are checking that c == 2 (because a prime number has only 2 factors 1 and itself)
then its a prime number
else not a prime number.!!!!!
'''
num = int(input("enter a number: "))
i = 1
c = 0
while i <= num:
    if num % i == 0:
        c += 1
    i += 1
if c == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")

# ---------------------------------------------------------------------------------------------------------------
# ----- complexity is o(n//2)
'''to reduce the complexity we can write the same prime num
  program  using this 
  There will not be any factors for a number after n//2. Right
'''

'''
here we are takeing that num as a user input.....
here variable i is initiated to 2 because every number is divisible by 1 so we start from 2
we are checking that factors from 2 and go upto n//2......
then if i less than or equal to n//2.....
'''
num = int(input("enter a num: "))
i = 2
while i <= num//2:
    if num % i == 0:
        print("Not a Prime Number")
        break 
    i += 1 
else:
    print("Prime Number")


# -----------------------------------------------------------------------------------------------------------------
#  Theorem: A prime number doesn't have any factors from 2 to square root of itself.
# ----- complexity is o(^n)
num = int(input("enter a num: "))
i = 2
sqr = int(num**0.5)
while i <= sqr:
    if num % i == 0:
        print("Not a Prime Number")
        break
    i += 1
else:
    print("Prime number")

# ------------------------------------------------------------------------------------------------------
# ------- using for loop -----
num = int(input("enter a num: "))
rt = int(num ** 0.5)
for i in range(2,rt+1):
    if num % i == 0:
        print("Not prime number")
        break 
else:
    print("Prime number")


# ------------------------------------------------------------------------------------
#  print the prime numbers from 1 to 50 ----
for num in range(1,51):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print("Not prime",num)
                break
        else:
            print("Prime",num)


# ------------   Prime Number Program in Functions using for loop  ----------
def Prime_number(num):
    rt = int(num**0.5)
    for x in range(2,rt+1):
        if num % i == 0:
            print("Not prime Number")
            break
    else:
        print("Prime Number")
# num = Prime_number(int(input("enter a number: ")))
num = Prime_number(int(input("enter a number: ")))
print(num)


# ------------------------------------------------------------------------------------------------
#  1 ST PRIME PROGRAM USING FUNCTIONS
def Prime_Number(n):
    i = 1
    c = 0
    while i <= n:
        if n % i == 0:
            c += 1
        i += 1
    if c == 2:
        print("Prime number ",n)
    else:
        print("Not Prime NUmber",n)
n = int(input("enter a number: "))
Prime_Number(n)


# 2ND PRIME NUMBER PROGRAM USING FUNCTIONS
def PrimeNumber(num):
    i = 2
    while i <= num//2:
        if num % i == 0:
            print("Not Prime ")
            break
        i += 1
    else:
        print("Prime NUmber")
num = int(input("enter a num: "))
PrimeNumber(num)


# 3 RD PRIME NUMBER PROGRAM USING FUNCTIONS (THEOREM)
def theorem_prime_num(num):
    i = 2
    sqr = int(num**0.5)
    while i <= sqr:
        if num % i == 0:
            print("Not a Prime Number")
            break
        i += 1
    else:
        print("Prime number")
num = int(input("enter a num: "))
theorem_prime_num(num)




# -----------------------------------------------
#  ANAGRAM PROGRAM
s1 = input("enter a s1: ")
s2 = input("enter a s2: ")
if sorted(s1) == sorted(s2):
    print("Anagram for each others")
else:
    print("NOt Anagram")


s1 = input("enter a s1: ")
s2 = input("enter a s2: ")
if len(s1) == len(s2):
    if sorted(s1) == sorted(s2):
        print("Anagram each other")
    else:
        print("Not Anagram")


