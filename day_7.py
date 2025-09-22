#Stack data structure LIFO
def find_peak(stack):
    if stack is not None:
        return stack[-1]
def is_empty(stack):
    if len(stack)==0:
        return True
    return False
def is_full(stack):
    if len(stack)==5:
        return True
    return False
stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop()) 
print(is_empty(stack))
print(is_full(stack))
