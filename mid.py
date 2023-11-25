### 1. What is the difference between append() and extend() methods?
"""
    append() = append function add single element to the end  of the list 
    extend() = extend will add all elements of an iterable (list,tuple,string) to end of list
        ( or )   add individual elements to the end of the list
"""

l1 = [1,3,5,6]
l2 = [34,56]
l1.append(100)
l2.append(l1)
print("appending elements",l1)
print("appending list of elements at end",l2)

list1 = [4,6,8,9]
list2 = [12,56]
list1.extend(list2)
print("Extending two lists",list1)


### 2. Write a program to create a dictionary as follows ?
##OUTPUT:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
emp_dic = {}
for i in range(1,16):
    emp_dic[i] = i**2
print(emp_dic)

### 3. Write a program to Check if a given number is a Palindrome or not? 
number = int(input("enter a number: "))
num = str(number)
if num[::] == num[::-1]:
    print("Given Number is Palindrome")
else:
    print("Not Palindrome")

### 4. Python program which  generate a list and a tuple which contains every number.Suppose the following
## input = 23,56,76,12,87  Then, the output should be:
## ['23', '56', '76', '12', '87']
## ('23', '56', '76', '12', '87')

num = 23,56,12,87
l = []
for i in num:
    l.append(str(i))
print("List of STring Numbers",l)
print("Tuple of String NUmbers",tuple(l))


#### 5.  Write a code to print “Python” for multiples of three instead of the number, 
## “Coding” for the multiples of five, “Python Coding” for multiples of both three and five (range is from 1 to 26)
for i in range(1,27):
    if i %3 == 0 and i%5 == 0:
        print(i,"Python Coding")
    elif i %5 == 0:
        print(i,"Coding")
    elif i%3==0:
        print(i,"Python")


### 1.What are the Immutable and Mutable built-in datatypes of Python Explain the feature immutable with suitable code
"""  Immutable : immutable data types are those that cannot be changed,update,delete after they are created 
  examples for immutable : str,int,float,tuple,frozen set  
  examples for mutable: list,set,dictionary  """

# t = (12,34,56)
# t[1] = 100
# print("Immutable data types",t)

l = [12,34,56]
l[1] = 100
print("Mutable data type",l)

s = {12,34,56}
s.add(100)
print("Mutable built in data type",s)

#### 3.Write a code to accept full name as a combination of first name and last name seperated by space.
##  Accept gender from user. Add appropriate salutation (Mr./Ms.) to the name. Display the output as given below?
firstname = input("Enter First Name: ")
lastname = input("Enter last name: ")
name = f"{firstname} {lastname}"
gender = input("enter [male/female]: ").lower()
if gender == "male":
    print(f"Mr. {name}")
else:
    print(f"Ms. {name}")


#### 4.  Write a code to add “alpha”:26 to the existing dictionary. (5 Marks)
## dic={'Eddy':13,'Maria':44,'Jas':21}

d = {'Eddy':13,'Maria':44,'Jas':21}
d["alpha"] = 26
print(d)

name = {'Eddy':13,'Maria':44,'Jas':21}
name.update({"alpha": 26})
print(name)


#### 5. Write a python program. Suppose the input=6 Then, the output should be:
### {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36} 
d = {}
n = int(input("enter num : "))
for i in range(1,n):
    d[i] = i*i
print(d)

num = int(input("enter num: "))
numbers = [x for x in range(1,num)]
sqr = [x*x for x in range(1,num)]
res = dict(zip(numbers,sqr))
print(res)


#### 6. Write a code to find the factors of  a given number? Write Recursive and non-recursive codes
n = int(input("enter a n: "))
for i in range(1,n+1):
    if n % i == 0:
        print(i,end=" ")

def fact(n):
    i = 1
    l = []
    if i < n and n % i  == 0:
        l.append(i)
        i += 1
        #return fact()
    else:
        return l
fact(10)     


### 7. For a given nested list find out the maximum element and calculate average of all elements.
## Use the given list?         list1 = [[20,25,30],[10,15,18],[12,45,20],35,20,23,28]
list1 = [[20,25,30],[10,15,18],[12,45,20],35,20,23,28]
l = []
for i in list1:
    if type(i) == list:
        l.extend(i)
    else:
        l.append(i)
print(l)
print(max(l))
res = sum(l)/len(l)
print(res)
