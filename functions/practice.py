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

# -------
def intro(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome to software industry")
intro("teja","dulam")

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
    res = x*y*z
    return s,avg, res
print(sum(10,20,30))

# ----parameter passing---
def add(x,y,z):# formal arguments
    sum = x+y+z
    return sum
a = 19
b = 29
print(add(a,15,b))# actual arguments


# types of arguments
# -----Positional arguments---
def mul(x,y):
    return x*y
print(mul(5,5))  #positional arguments


# ----- default arguments---
def avg(x,y,z=5):
    sum = x+y+z

    return sum
print(avg(10,20))# z takes default value 5
print(avg(10,20,30))# z is 5 it replace by the actual argument by 30

# ---- variable arguments---
def add(*args):
    print(type(args))# tuple
    s = 0
    for x in args:
        s = s+x
    return s
print(add(2,4,5))


def mul(*args):
    v = 1
    for x in args:
        v *= x
    return v
print(mul(2,3))


# -------varaiable keyword arguments---
def self(**data):
    print(type(data))
    return data
print(self(id = 100, name = "teja", age = 20 ))

def intro(**data):
    for key, value in data.items():
        print(key, value)
    return data
print(intro(name = "teja", id = 1001, phno = 23456))