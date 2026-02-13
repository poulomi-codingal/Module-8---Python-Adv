class Parrot:

    #class attribute
    species = "bird"

    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
obj1 = Parrot("Blue", 10)
obj2 = Parrot("red",  12)

print("Obj1 is a {}".format(obj1.species))
print("Obj2 is a {}".format(obj2.species))

print("Obj1 is {} and it is {} years old".format(obj1.name, obj1.age))

print("Obj2 is {} and it is {} years old".format(obj2.name, obj2.age))


