grades=[('alice', 'A'), ('bob', 'B'), ('charlie', 'C')]
dict_grades={name:grade for name,grade in grades}
print(dict_grades)
for name,grade in dict_grades.items():
    print(f"Student :{name}, Grade :{grade}")