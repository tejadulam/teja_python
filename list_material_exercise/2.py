# Write a program to convert a list of characters into a single string.
# Sample Input: ["a","b","c","d"]
# output: abcd

l = ["a","b","c","d"]
for x in l:
    print(x,end="")
print()

# another way
l = ["a","b","c","d"]
s = "".join(l)
print(s)