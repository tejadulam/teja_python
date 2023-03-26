#  program to modify or replace an existing element of a tuple with a new element.

t = (23,45,67,88)
l = list(t)
l[2] = 200
print(tuple(l))