def find_second_largest(arr):
    first=second=float('-inf')
    for num in arr:
        if num>first :
            second=first
            first=num
        elif num<first and num>second:
            second=num
    return second if second!=float('-inf') else None

arr=[12,35,1,10,34,1]
print(find_second_largest(arr))