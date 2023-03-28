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


