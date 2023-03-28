words = ["Apple", "Orange", "Apple",
        "Banana", "Peach", "Banana",
        "Apple", "Peach", "Apple",
          "Banana"]
count = {}
for x in words:
    if x not in count:
        count[x] = 1
    else:
        count[x] += 1
print(count)
print("Mxmimum count:" ,max(count.items() , key= lambda x:x[1]))
print("minimum count:" ,min(count.items(), key = lambda x:x[1]))
print(sorted(count.items(),key = lambda x:x[1]))
print(sorted(count))