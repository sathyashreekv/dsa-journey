#implementaion of Queue

#A queue is a linear data structure which follows fifo order 
#element which added first will be one removed first
'''Enqueue - add element to the end of the queue using rear pointer
   Dequeue - remove elements from the front of the queue using front pointer
    Peek - get the front element of the queue
    isEmpty - check if the queue is empty
    isFull - check if the queue is full
    size - get the number of elements in the queue
    display - display all elements in the queue

'''
#using list
queue=[]
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
print(queue.pop(0))
print(queue.pop(0))
print(queue)

#using collections module
from collections import  deque
"""
dequeue is preferred over the list because i taks o(1) time for appending and poppong elements from both ends
whereas list takes o(n) time for popping elements from the front of the list"""

q=deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(q)
print(q.popleft())
print(q.popleft())
print(q)
