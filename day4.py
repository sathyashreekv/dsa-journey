my_list=[13,5,22,9,41,19]
min=float('inf')
max=float('-inf')
for i in range(len(my_list)):
    if my_list[i]>max:
        max=my_list[i]
    if my_list[i]<min:
        min=my_list[i]
print("The largest element :",max,". The smallest element is :",min)

number=int(input("Add a number to my bag :"))
my_list.append(number)
for x in my_list:
    print(x, end=" ")
print("want to add your fav number at a specific position ? then level up ")
val=int(input("Enter the value :"))
pos=int(input("Enter the position you want to add :"))
my_list.insert(pos,val)
for x in my_list:
    print(x, end=" ")
del_num=int(input("Want to remove a number :"))
my_list.remove(del_num)
for x in my_list:
    print(x, end=" ")
my_list.sort()
for x in my_list:
    print(x, end=" ")