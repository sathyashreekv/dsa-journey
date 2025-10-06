import heapq
from typing  import List

def sum_between(nums:List[int],k1:int,k2:int)->int:
    nums.sort()
    return sum(nums[k1:k2-1])

def min_heapify(nums:List[int],i:int,n:int)->None:
    small=i
    l=2*i+1
    r=2*i+2
    if l<n and nums[l]<nums[small]:
        small=l
    if r<n and nums[r]<nums[small]:
        small=r
    if small!=i:
        nums[small],nums[i]=nums[i],nums[small]
        min_heapify(nums,small,n)

def sumBetweenk1k2(nums:List[int],k1:int,k2:int)->int:
    n=len(nums)
    ans=0
    for i in range((n//2)-1,-1,-1):
        min_heapify(nums,i,n)
    k1-=1
    k2-=1
    for i in range(k1+1):
        nums[0]=nums[n-1]
        n-=1
        min_heapify(nums,0,n)
    for i in range(k1+1,k2):
        ans+=nums[0]
        nums[0]=nums[n-1]
        n-=1
        min_heapify(nums,0,n)
    return ans


nums=[20,8,22,4,12,10,14]
print(sumBetweenk1k2(nums,3,6))