my_set = {1, 4, 1, 23, 2, 4, 87, 34.5}
print(my_set)
my_set.add(6)
print("Updated set : ",my_set)

set1= my_set
set2= {3,5, 6,8}

print("Set1",set1)
print("Set2",set2)

print("Difference")
print(set1.difference(set2))

print("Symmetric Difference")
print(set1.symmetric_difference(set2))

set_u = set1.union(set2)
set_i = set1.intersection(set2)

print("Set Union", set_u)
print("Set Intersection", set_i)



