def sum_pair(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        if arr[left]+arr[right]==target:
            return True
        elif arr[left]+arr[right<target]:
            left+=1
        else:
            right+=1
    return False

arr=[2,5,8,11,14]
target=16
print(sum_pair(arr,target))