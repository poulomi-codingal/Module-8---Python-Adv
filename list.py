list1 = ["Orange", "Red", "Green", "Yellow","White", "Black", "Pink", "brown"]

print(" Initial List elements : ", list1)
print("Length of the list", len(list1))
print("First element in the list ", list1[0])
print("Last element in the list", list[-1])

list1.append("Mango")
print("Updated list : ", list1)

list1.remove("Yellow")
print("Updated list : ", list1)

list1.sort()
print("After sorting list :", list1)

list1.pop(1)
print("after pop operation : ", list1)

list1.reverse()
print("After reverse operation : ", list1)

print("Multiplication on list : ",list1*2)

list1 = list1[:4]
print(list1)

list1.clear()
print(list1)