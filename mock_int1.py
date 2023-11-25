## 1:  write a program to count the occurrence of each word in the text given below

# ------------------ using with an empty dict
sentence = """Through three cheese trees three free fleas flew
     While these fleas flew freeze breeze blew
     Freeze breeze made these three trees freeze
     Freeze trees made these trees cheese freeze
     That's what made these three free fleas sneeze """
res = sentence.lower().split()
d = {}
for word in res:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
print(d)

# ------ using counter
from collections import Counter
sentence = """Through three cheese trees three free fleas flew
     While these fleas flew freeze breeze blew
     Freeze breeze made these three trees freeze
     Freeze trees made these trees cheese freeze
     That's what made these three free fleas sneeze """
res = sentence.lower().split()
cnt = Counter(res)
print(cnt)

# ---- using default dict
from collections import defaultdict
d = defaultdict(int)
sentence = """Through three cheese trees three free fleas flew
     While these fleas flew freeze breeze blew
     Freeze breeze made these three trees freeze
     Freeze trees made these trees cheese freeze
     That's what made these three free fleas sneeze """
res = sentence.lower().split()
for words in res:
    d[words] += 1
print(d)


"""2. You can climb to the top in n distinct ways. Here's a Python program that calculates it:
python"""

def ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return ways(n-1) +ways(n-2)
print(ways(5))


"""3. Here's a Python program that reads n mobile numbers from the user and then prints them in the standard format:
python"""

n = int(input("enter a num: "))
numbers = []
for _ in range(n):
    numbers.append(input())

def format_numbers(func):
    def wrapper(numbers):
        for number in numbers:
            func("+91 " + number)
    return wrapper

@format_numbers
def print_numbers(number):
    print(number)

print_numbers(numbers)

