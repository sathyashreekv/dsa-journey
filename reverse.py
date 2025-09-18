my_list=[1,2,3,4,5,6,7,8,9,10 ]
for i in range(len(my_list)//2):
    temp=my_list[i]
    print(temp)
    my_list[i]=my_list[len(my_list)-1-i]
    print(my_list[i])
    my_list[len(my_list)-1-i]=temp
    print(my_list[len(my_list)-1-i])
for x in my_list:
    print(x, end=" ")