class Person :

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print(self.fname, self.lname)

class Student(Person):

    def __init__(self,fname,lname,year):
         self.year = year
         super().__init__( fname,lname)

obj1 = Student("Rahul", "Meheta", 2009)

obj1.display()

print(obj1.year)