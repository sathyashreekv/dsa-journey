my_list=[1,2,3,2,4,3,5,1,6,7,8,9,7]
new_list=[]
for i in range(len(my_list)):
    if my_list[i] not in new_list:
        new_list.append(my_list[i])
for x in new_list:
    print(x, end=" ")