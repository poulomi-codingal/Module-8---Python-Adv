#if your list has more than 3 elements
list_1 = [(1, "Rahul", "V"), (2, "Ron", "III"),(3, "Vivek", "II"), (4, "Dipak", "VI"), (5, "Bony", "VII")]


#if your list has 2 elements 
list_2 = [("BMW","Red"), ("Nano", "White"), ("Tata", "Black"), ("Honda", "Grey")] 
my_dict = dict(list_2)
print(my_dict)


#writing function for taking all three elements into dict .. 
def test(list_emp):
    result = {}
    for item in list_emp:
        result[item[0]] = item[1:]
    return result
    
print(list_1)
print(test(list_1))