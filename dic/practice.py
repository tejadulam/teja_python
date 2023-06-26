d = {"Resturantname":"cherla's",
     "starters":"hongkong-chicken",
     "drinks": 4,
     "bill":560.6
     }
print(d)
print(type(d))
print(list(d.items()))

d["starters"] = "dilkushbiryani"  #-----to add a key value pair in dictionary, if the key already exist it will update the value
print(d)
print(d["bill"])

print(d.items())
print(list(d.items()))  #----list of tuples
d["starters"] = "chickenlollipops"
print(d)

print(list(d.keys()))
print(d.values())
print(d["Resturantname"])

d.pop("bill")  #---entire key and value will delete
print(d)

# ********************************************************************************************
"----------------------------- DICTIONARY USE CASES ----------------------------                                                           "


# -----------------------------------------------------------------------------
#         COUNTING PROBLEM

words = ["Apple", "Orange", "Apple", "Banana", "Peach",  
          "Banana", "Apple", "Peach", "Apple", "Banana"]
count = {}
for word in words:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1
print(count)
print("Maximum count" ,max(count.items(),key = lambda x:x[1]))
print("Minimum count" ,min(count.items(),key = lambda x:x[1]))
print(sorted(count.items(),key = lambda x:x[1]))
print(sorted(count.items(),key = lambda x:x[1],reverse = True))


# ------------------------------------------------------------------------------
#           GROUPING PROBLEM
trans = [(1237, 87522),
 (1234, 1000),
 (1236, 6754),
 (1234, 200),
 (1236, 1700),
 (1234, 400),
 (1234, 600),
 (1236, 788),
 (1234, 500),
 (1237, 126653),
 (1999, 1000)]

dep = {}
for id , amount in trans:
    if id not in dep:
        dep[id] = [amount]
    else:
        dep[id].append(amount)
print(dep)
print(max(dep.items()))
print(max(dep.items(), key = lambda x:len(x[1])))

print(len(dep))



# -------------------------------------------------
#            COLLECTION
# from collections import counter
# fruits = ["Apple", "Orange", "Banana", "Peach", "Apple",
# "Banana", "Apple", "Peach", "Apple", "Banana"]
# cnt = counter(fruits)
# print(cnt)


"""
    1:Write a program to prompt the user to give name and marks of 5 different students,
      store them in dictionary and print it after sorting the dictionary with respect to their marks.
"""
d = {}
for i in range(5):
    stud = input("enter a stud: ")
    marks = int(input("enter a marks: "))
    d[stud] = marks
print(d)


"""
    2: Use the dictionary given below whose keys are month names and whose values are the number of days in the corresponding months.
(a) Ask the user to enter a month name and use the dictionary to tell them how many days are in the month.
(b) Print out all of the keys in alphabetical order.
(c) Print out all of the months with 31 days.
days = { ' January ' : 31, ' February ' : 28, ' March ' : 31, ' April ' : 30,
 ' May ' : 31, ' June ' : 30, ' July ' : 31, ' August ' : 31,
 ' September ' : 30, ' October ' : 31, ' November ' : 30, ' December ' : 31}
"""
days = { ' January ' : 31, ' February ' : 28, ' March ' : 31, ' April ' : 30,
        ' May ' : 31, ' June ' : 30, ' July ' : 31, ' August ' : 31,
        ' September ' : 30, ' October ' : 31, ' November ' : 30, ' December ' : 31}
print(days[' April '])
print(days[' February '])
print(sorted(days.keys()))


"""
    3: Write a program to count the number of characters (character frequency) in a string.
# Sample Input
 'google'
# Expected Output
 {'g': 2, 'o': 2, 'l': 1, 'e': 1}
"""
word = "google"
d = {}
for i in word:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)


"""
    4: Write a program to count the number of occurrences of each letter in word "MISSISSIPPI". 
    Store count of every letter with the letter in a dictionary and print the sorted 
    dictionary according to the count of letters.
"""
s = "MISSISSIPPI"
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)

"""
    5: Write a program to count the occurrences of each word in the text given below.
"""
sentence = """Through three cheese trees three free fleas flew
     While these fleas flew freezy breeze blew
     Freezy breeze made these three trees freeze
     Freezy trees made these trees cheese freeze
     That's what made these three free fleas sneeze """
res = sentence.lower().split()
d = {}
for word in res:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
print(d)

"""
   6:   Write a program to get the frequency of the elements in a list.
    # Sample Input
     [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
    # Expected Output
     {10 : 4, 20 : 4, 40 : 2, 50 : 2, 30 : 1}
"""
list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
d = {}
for x in list:
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1
print(d)


"""
  7:   Write a program to concatenate following dictionaries to create a new one.
    # Sample Input
     dic1 = {1 : 10, 2 : 20}
     dic2 = {3 : 30, 4 : 40}
     dic3 = {5 : 50, 6 : 60}
    # Expected Output
     {1 : 10, 2 : 20, 3 : 30, 4 : 40, 5 : 50, 6 : 60}

"""
dic1 = {1 : 10, 2 : 20}
dic2 = {3 : 30, 4 : 40}
dic3 = {5 : 50, 6 : 60}
new = {}
new.update(dic1)
new.update(dic2)
new.update(dic3)
print(new)

"""
    8: Write a program to print a dictionary where the keys are numbers 
        between 1 and 15 (both included) and the values are square of keys.
    Expected Output:
     {1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100,
        11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
"""
d = {}
for i in range(1,16):
    d[i] = i**2
print(d)

"""
    9: Write a Python program to print the sum all the values in a dictionary.
    Sample Input: {'data1' : 100, 'data2' : 54,'data3' : 247}
    Expected Output:  293
"""

data = {'data1' : 100, 'data2' : -54,'data3' : 247}
print(sum(data.values()))


# -----------------------------------------------------------------
#  Factors from 1 to 10 and num as a key factor as a value
d = {}
f = 1
for i in range(1,11):
    f *= i
    d[i] = f
print(d)

"""
    Write a program that reads through any dictionary given below and prints the following:
(a) All the users whose phone number ends in an 8
(b) All the users that do not have an email address listed

"""
# d = [
#     { ' name ' : ' Todd ' , ' phone ' : ' 555-1414 ' , ' email ' : ' todd@mail.net ' },
#      { ' name ' : ' Helga ' , ' phone ' : ' 555-1618 ' , ' email ' : ' helga@mail.net ' },
#      { ' name ' : ' Princess ' , ' phone ' : ' 555-3141 ' , ' email ' : '' },
#      { ' name ' : ' LJ ' , ' phone ' : ' 555-2718 ' , ' email ' : ' lj@mail.net '}
#     ]

