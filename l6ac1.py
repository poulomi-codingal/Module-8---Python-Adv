class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"Hi I am {self.name} . My age is {self.age} years old")


    def make_sound(self):
        print("Meow...")

class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"Hi I am {self.name} . My age is {self.age} years old")

    def make_sound(self):
        print("Barking ...")

cat1 = cat("Lily", 4)
dog1 = dog("Ramba", 7)

for animal in(cat1,dog1):
    animal.make_sound()
    animal.intro()