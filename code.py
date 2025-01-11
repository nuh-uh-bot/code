nub = int(input("Enter number of students: "))
names = []
holder = {}

for i in range(0, nub):
    name = input("Enter name of student: ")
    add_no = int(input(f"Enter addmission number of {name}: "))
    holder[name] = add_no
    names.append(name)
    
total_names = len(names)

for a in range(0,total_names):
    name_find = names[a]
    print(f"Name: {name_find}, Admission Number: {holder[name_find]}")
