my_dict={
    "name":"sathya",
    "age":19,
    "city":"Pavagada"
}
print(my_dict["name"])
print(my_dict['age'])
my_dict['age']=20
print(my_dict['age'])
my_dict['Country']='India'
print(my_dict)
print(my_dict.pop('city'))
print(my_dict.popitem())

for key in my_dict:
    print(key)
for value in my_dict.values():
    print(value)
for key,value in my_dict.items():
    print(f"{key}:{value}")
