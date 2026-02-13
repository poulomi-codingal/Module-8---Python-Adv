class Student:
    grade = 9
    name = "Disha"
    def f1(st):
        print("hello world .. Disha ")
    
    def f2(st):
        print("Student name :", st.name)
        print("Student Grade :", st.grade)

obj1 = Student()
obj1.f1()
obj1.f2()