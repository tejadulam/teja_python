# count the computer in given data

students = [ ("John", ["Computers", "Physics", "Maths"]), 
             ("Wasim", ["Maths", "Computers", "Statistics"]),
             ("Naresh", ["Computers", "Accounting", "Economics"]), 
             ("SaiTeja", ["English", "Accounting", "Economics", "Law"]), 
             ("Sravani", ["Sociology", "Economics", "Law", "Stats", "Music"])]
count = 0
for x in students:
    if "Computers" in x[1]:
        count+=1
print(count)
