
##------ 1. A list is supposed to contain first n natural numbers in it. But one number is missing
##  in the list. so, we have n-1 elements in the list. How do you find the missing element?
def missing_number(n,lst):
    exp_sum = n*(n+1)//2
    actual_sum = sum(lst)
    return exp_sum - actual_sum
n = 10
lst = [1,3,4,5,6,7,8,9,10]
print(missing_number(n,lst))



###------- 2. How do you check two lists are having the same set of values and the same number of values?
list1 = [1,3,5,7]
list2 = [7,5,3,1]
if set(list1) == set(list2) and len(list1) == len(list2):
    print("List having same set of values")
else:
    print("Not having same set of values")



"""------- 3. A list of email ids(strings) given, and assume there is a third-party function "send_email()" is available.
 Imagine "send_email(email id, msg)" takes email address and message as parameters.
For instance, send_email('john@abc.com', 'Welcome to my birthday!') sends a message 
'Welcome to my birthday!' to 'john@abc.com'. Write a program to send an invitation message, 
to all the email ids in the list. Do not send message to email ids having hotmail.com in it."""

emails = [
'john.deer@gmail.com',
'alex.barner@yahoo.com',
'brad.cooper@hotmail.com',
'cindy.barner@hotmail.com',
'matt.damon@gmail.com',
'george.cloony@yahoo.com',
'mc.barner@hotmail.com'
]
for mail in emails:
    if  "hotmail.com" not in mail:
        print(f"{mail},Welcome to my Birthday")



"""-----4. Below are the customer ids and deposits are done by customers on a typical day of a bank.
 Write a program to answer the following.
"""

## ------4(1): How many distinct customers deposited the money? 
transactions = [(1237, 87522),
(1234, 1000),
(1236, 6754),
(1234, 200),
(1236, 1700),
(1234, 400),
(1234, 600),
(1236, 788),
(1234, 500),
(1237, 126653)
]
cu = {}
for ac_id,amount in transactions:
    if  ac_id not in cu:
        cu[ac_id] = [amount]
    else:
        cu[ac_id].append(amount)
print("Distinct customers in the transaction",len(cu))

## ---------4(2): Who deposited a maximum number of times?
transactions = [(1237, 87522),
(1234, 1000),
(1236, 6754),
(1234, 200),
(1236, 1700),
(1234, 400),
(1234, 600),
(1236, 788),
(1234, 500),
(1237, 126653)
]
cu = {}
for ac_id,amount in transactions:
    if  ac_id not in cu:
        cu[ac_id] = [amount]
    else:
        cu[ac_id].append(amount)
max_dep = max(cu.items(),key=lambda x:len(x[1]))
print("The customer deposited a maximum number of times",max_dep)

##------ 4(3): Who deposited the maximum sum of deposits?
transactions = [(1237, 87522),
(1234, 1000),
(1236, 6754),
(1234, 200),
(1236, 1700),
(1234, 400),
(1234, 600),
(1236, 788),
(1234, 500),
(1237, 126653)
]
cu = {}
for ac_id,amount in transactions:
    if  ac_id not in cu:
        cu[ac_id] = [amount]
    else:
        cu[ac_id].append(amount)
max_sum = max(cu.items(),key=lambda x:sum(x[1]))
print("The customer deposited a maximum sum of deposits",max_sum)

# ##-------- 4(4): Who deposited the maximum amount in a single transaction?
transactions = [(1237, 87522),
(1234, 1000),
(1236, 6754),
(1234, 200),
(1236, 1700),
(1234, 400),
(1234, 600),
(1236, 788),
(1234, 500),
(1237, 126653)
]
cu = {}
for ac_id,amount in transactions:
    if  ac_id not in cu:
        cu[ac_id] = [amount]
    else:
        cu[ac_id].append(amount)
max_sum = max(cu.items(),key=lambda x:(x[1]))
print("The customer deposited a maximum amount in single transaction",max_sum)

#--------  4(5): Print all Customer Id's and list of deposits done by each customer.
transactions = [(1237, 87522),
(1234, 1000),
(1236, 6754),
(1234, 200),
(1236, 1700),
(1234, 400),
(1234, 600),
(1236, 788),
(1234, 500),
(1237, 126653)
]
cu = {}
for ac_id,amount in transactions:
    if  ac_id not in cu:
        cu[ac_id] = [amount]
    else:
        cu[ac_id].append(amount)
print("All the costumer id and their deposits",(cu))


#------- 4(6): Print total balance at the end of the day.
transactions = [(1237, 87522),
(1234, 1000),
(1236, 6754),
(1234, 200),
(1236, 1700),
(1234, 400),
(1234, 600),
(1236, 788),
(1234, 500),
(1237, 126653)
]
res = sum(t[1] for t in transactions)
print("Total balance at end of the day is ", res)


###-----5. List of votes, contestants and ages are given. Write a program to 
# find the contestant who wins the elections. If there is a tie, older contestant wins.
votes = [
       'Kenny', 'Amanda', 'John', 'Vicky', 'Alex',
       'Amanda', 'John', 'Alex', 'Kenny', 'Vicky',
      ';Charles', 'Alex', 'Kenny', 'Eric', 'Charles',
       'Eric', 'Laura', 'Michelle', 'Eric', 'Vicky'
]
d = {}
for words in votes:
    if words not in d:
        d[words] = 1
    else:
        d[words] += 1
age = {
'Kenny': 61,
'Amanda': 54,
'Alex': 79,
'John': 80,
'Vicky': 34,
'Eric': 50,
'Laura': 55,
'Michelle': 42,
'Charles': 70
}
wining_vote = None
for vote in d:
    if wining_vote is None or d[vote] > d[wining_vote] or d[vote] == d[wining_vote] and age[vote] > age[wining_vote]:
        wining_vote = vote
print(" Who win ths election ",wining_vote)


###------ 6. Check the given two strings are anagrams or not.
word1 = input("enter a word: ")
word2 = input("enter a word: ")
if sorted(word1) == sorted(word2):
    print("Given Strings are Anagrams")
else:
    print("Not Anagrams")


###------- 7. Write a program to find all sets of anagrams when a list of words given.

list1 = ["listen","silent","ate","ate","xyz","abc","cba"]
ana = {}
for word in list1:
    sorted_word = "".join(sorted(word))
    if sorted_word  in ana:
        ana[sorted_word].append(word)
    else:
        ana[sorted_word] = [word]
for text,texts in ana.items():
    if len(texts) > 1:
        print(texts)


###------- 8. Solve the following – by printing specific items from the list given below.
"""Print the value 2000 on your screen.
Print the dictionary of the cities and states on your screen.
Print the list of the clothes on your screen.
Print the word 'Phoenix' on your screen.
Print the word 'jeans' on your screen.
Print the word 'blue' on your screen.
test = [{'Arizona': 'Phoenix', 'California': 'Sacramento', 'Hawaii': 'Honolulu'},1000,2000,3000,
['hat', 't-shirt', 'jeans', {'socks1': 'red', 'socks2': 'blue'}]
]
"""
test = [{'Arizona': 'Phoenix',
        'California': 'Sacramento', 
       'Hawaii': 'Honolulu'},

        1000,2000,3000,['hat', 't-shirt', 'jeans', {'socks1': 'red', 'socks2': 'blue'}]
]
print("Print the value 2000 on your screen",test[2])

print("Print the dictionary of the cities and states on your screen",test[0])

##----- Print the list of the clothes on your screen
print(test[4])

##------ Print the word 'Phoenix' on your screen.
res = test[0]
print(res["Arizona"])

#------- Print the word 'jeans' on your screen.
print(test[4][2])

#------ Print the word 'blue' on your screen.
res = test[4][3]
print(res["socks2"])