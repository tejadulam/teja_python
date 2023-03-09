n = input()
s = n[0]
for i in range(len(n)):
    if n[i]!=s[-1]:
        s+= n[i]
print(s)