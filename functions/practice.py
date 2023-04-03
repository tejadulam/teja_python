#  ----simple addition program in function
def add(x,y):
    sum = x+y
    return sum
print(add(10,30))

def sum(x,y,z):
    print("Addition of three numbers")
    return x+y+z
print(sum(10,20,30))
print(sum(23,45,67))

# ----factorial ncr ----
def fact(n):
    f = 1
    for x in range(1,n+1):
         f *= x
    return f
print(fact(5))
def ncr(n,r):
    res = fact(n)/(fact(n-r)*fact(r))
    return res
print(ncr(5,2))

# ------returning multiple values
def sum(x,y,z):
    s = x+y+z
    avg = s/3
    return s,avg
print(sum(10,20,30))

# ----parameter passing---
def add(x,y,z):# formal arguments
    sum = x+y+z
    return sum
a = 19
b = 29
print(add(a,15,b))# actual arguments
