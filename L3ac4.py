class Parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    def dance(self):
        return "{} is now dancing ".format(self.name)
    
obj1 = Parrot("Bluey",10)

print(obj1.sing("La la la..."))
print(obj1.dance())



