class Employee:

    def __init__(self):
        print("Employee created ..")
    def __del__(self):
        print("Destructor called , employee deleted ...")

emp1 = Employee()
del emp1
