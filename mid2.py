#### QUESTION : 1
""" 1. Ram built his own house and was confused about what name he should keep for it.
  He asked his friend Shyam to help. Shyam suggested a lot of names. Ram has certain conditions for the name:                                                                                                                    

#   It should consist of exactly three distinct characters, say C1, C2 and C3
#   It should satisfy the criteria that the string was of the form - C1n C2n C3n: This means,
 first C1 occurs n times, then C2 occurs n times and then C3 occurs n times.

# For example, xyz, ccaarr, mmmiiiaaa satisfy the criteria, but xyzw, aabbbcccc don't.
Given N names suggested by Shyam, print "OK" if Ram likes the name and "Not OK" if he doesn't.

# Input:
First-line contains a single positive integer N - the number of names.
N lines follow - each line contains a name.	

# Output:
For each name, Print "OK" if the name satisfies the criteria, else print "Not OK", on a new line.
Constraints:
1 ≤ N ≤ 100 1 ≤ Length of names ≤ 500
Names contain only lowercase English alphabets

# SAMPLE INPUT: 2
bbbrrriii
brian

# SAMPLE OUTPUT
OK
Not OK  """


















#### 2. You are  working with NASA and suddenly you got an opportunity to travel to the moon.
#  You have to stay there for 15 years.

"""
#  Exercise1: You have to calculate your weight in kilograms on the moon in a period of 15 years,(3 marks)
 
 Step1: Measure your Weight on the Moon and also create a variable to store it. Assume your starting weight:30
 
● For each year, you can calculate the new weight by adding a kilogram, and then multiplying by 6.5 percent (0.65)
 to get the weight on the moon:
 
#  Exercise2: Create basic Moon Weight Function: The function should take two parameters: current weight:30 and
   increased weight:0.5 (the amount the weight will increase each year)   
 
 Note: moon_weight = weight * 0.65
"""
## EXERCISE 1
your_weight_on_moon = {}
weight = 30
for i in range(1,16):
    weight += 1
    your_weight_on_moon[i] = round(weight*0.65,2)
print(your_weight_on_moon)

## EXERCISE 2
def cal_moon_weight(current_weight , increased_weight):
    moon_weight = round(current_weight*0.65,2)
    return moon_weight

weight_moon = 30
cur_weight = 1
moon = {}
for i in range(1,16):
    weight_moon += cur_weight
    moon[i] = weight_moon,cur_weight
print(moon)






#### 3. A famous hotel is maintaining its order history in the dictionary in the given format. Find out which food item is ordered the most
## order_id: [list of items ordered]
## order_history= {165:['Noodles','Tomato Soup','Fries'],168:['Rice Idly','Rawa Dosa','Fries'],190:['Fries','Noodles']}

order_history= {165:['Noodles','Tomato Soup','Fries'],168:['Rice Idly','Rawa Dosa','Fries'],190:['Fries','Noodles']}
order_items = {'Noodles':0,'Tomato Soup':0,'Fries':0,'Rice Idly':0,'Rawa Dosa':0,}

for items in order_history:
    for id in order_history[items]:
        if id in order_items.keys():
            order_items[id] += 1
print("List of Items: ",list(order_items.keys()))
most_ordered = max(order_items.items() , key=lambda x:x[1])
print("Most Ordered item: ",most_ordered[0])


#### 4. Write a Python program to make a currency converter. The currency converter should be able to convert a 
## specific currency to an appropriate INR (Indian National Rupee) value
"""
1. USD (U.S Dollars) (1 USD =71.83 INR)
2. YEN (Japanese YEN)  (1 YEN= 0.66 INR
3. EURO (1 EURO=79.57 INR) 
4. U.K. POUND (1 U.K POUND=93.11 INR)

INPUT AND OUTPUT SAMPLE:
Enter the currency which you want to convert. e.g. USD
Enter the value of the currency which you want to convert. e.g. 100
The total converted value is 7183.0 """

currency_convert = {"USD" : 71.83,"YEN": 0.66,"EURO": 79.57,"UK": 93.11}
currency = input("enter currency which you want to convert USD,YEN,EURO,UK: ")
amount = float(input("enter amount which you want to convert : "))
if currency in currency_convert:
    amount_IND = amount * (currency_convert[currency])
    print(amount_IND)
    

##### 5. A Basket of Halloween candy has an unknown amount of candy and you need to guess exactly
"""how much candy is in the bowl. You ask the person in charge a few questions to make a correct guess.
If the candy is divided evenly among 5 people, how many pieces would be leftover? The answer is 2 pieces.
You then ask about dividing the candy evenly among 6 people, and the amount left over is 3 pieces.Finally, 
you ask about dividing the candy evenly among 7 people, and the amount left over is 2 piecesBy looking at the bowl,
you can tell that there are less than 200 pieces. Write a program to determine how many pieces are in the bowl.            
     	
1. SAMPLE INPUT:
If the candy is divided evenly among 5 people, how many pieces would be leftover? : 2
If the candy is divided evenly among 6 people, how many pieces would be leftover? : 3
If the candy is divided evenly among 7 people, how many pieces would be leftover? : 2
  1. SAMPLE OUTPUT:
Number of candies in the jar: 177

2. SAMPLE INPUT :
If the candy is divided evenly among 5 people, how many pieces would be leftover? : 2
If the candy is divided evenly among 6 people, how many pieces would be leftover? : 4
If the candy is divided evenly among 7 people, how many pieces would be leftover? : 2
2. SAMPLE OUTPUT :
Number of candies in the jar: 142 """

candies_div = {5:int(input("enter pieces left over: ")),
              6:int(input("enter pieces left over: ")),
                7:int(input("enter pieces left over: "))}
for candy in range(1,200):
    if candy < 200 and candy % 5 == candies_div[5] and candy % 6 == candies_div[6] and candy % 7 == candies_div[7]:
        print("Number of Candies in The Jar : ",candy)
