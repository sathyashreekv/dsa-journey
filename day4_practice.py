def rotate(arr,d):
    n=len(arr)
    d=d%n
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)

def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
my_list=[1,2,3,4,5,6,7,8,9,10 ]
rotate(my_list,3)
for x in my_list:
    print(x, end=" ")