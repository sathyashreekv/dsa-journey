from collections import deque

def display(queue):
    if len(queue)==0:
        print("Queue is empty")
    else:
        print("Queue elements are:",end=" ")
        for i in queue:
            print(i,end=" ")
    print()

def enqueue(queue,item):
    queue.append(item)
    print(f"Enqueued: {item} ")
    display(queue)

def dequeue(queue):
    if len(queue)==0:
        print("Queue is empty")
        return None
    item=queue.popleft()
    print(f"Dequeued :{item}")
    display(queue)
    return item

def peek(queue):
    if len(queue)==0:
       print("queue is empty")
    else:
        print(f"Front element is :{queue[0]}")

def isEmpty(queue):
    if len(queue)==0:
        print(f"Queue is empty")
        return True
    else:
        print(f"Queue is not empty")
        return False
    return False
def isFull(queue,max_size):
    if len(queue)==max_size:
        print("Queue is full")
        return True
    else:
        print("Queue is not full")
        return False
    return False
def size(queue):
    print(f"Size of queue is :{len(queue)}")
    return len(queue)
def main():
    queue=deque()
    max_size=5
    isEmpty(queue)
    isFull(queue,max_size)
    enqueue(queue,10)
    enqueue(queue,20)
    enqueue(queue,30)
    enqueue(queue,40)
    enqueue(queue,50)
    isEmpty(queue)
    isFull(queue,max_size)
    size(queue)
    peek(queue)
    dequeue(queue)
    dequeue(queue)
    dequeue(queue)
    dequeue(queue)
    dequeue(queue)
    dequeue(queue)  # trying to dequeue from empty queue
    isEmpty(queue)
    isFull(queue,max_size)

if __name__=="__main__":
    main()