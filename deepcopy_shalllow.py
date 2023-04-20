# ---- Normal Copy 
l = [12,89,34,56]
p = l
print(l)
print(p)

# ---- Shallow Copy
l = [12,34,56,89,90]
p = l.copy()
print(l,"and",p)
p[2] = 88
print(l,"and",p) #---it copys only that list not other list

'''----here in shallow copy the inner elemnts also and aply 
to both the lists'''
s1 = [12,34,56,[3,5],12]
s2 = s1.copy()
s1[3][0] = 100
print(s1)
print(s2)

# ---- Deep Copy
import copy
l1 = [12,34,[99,33],22]
l2 = copy.deepcopy(l1)
print(l1,l2)
l2[2][0] = 100#--- this copy to only l2 not to l1 called as deep copy
print(l1)
print(l2)