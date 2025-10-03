class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    if root.val==key:
        return root
    if root.val<key:
        root.right=insert(root.right,key)
    else:
        root.left=insert(root.left,key)
    return root

def search(root,key):
    if root is None or root.val==key:
        return root
    if root.val<key:
        return search(root.right,key)
    else:
        return search(root.left,key)
def get_inorder_successor(root):
    curr_node=root.right
    while curr_node is not None and curr_node.left is not None:
        curr_node=curr_node.left
    return curr_node
def delete(root,key):
    if root is None:
        return root
    if key<root.val:
        root.left=delete(root.left,key)
    elif key>root.val:
        root.right=delete(root.right,key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        temp=get_inorder_successor(root)
        root.val=temp.val
        root.right=delete(root.right,temp.val)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
r=Node(50)
r=insert(r,30)
r=insert(r,20)
r=insert(r,40)
r=insert(r,70)
r=insert(r,60)
r=insert(r,80)
inorder(r)
print("Found" if search(r,80) else "Not Found")
print("Found" if search(r,90) else "Not Found")
x=80
root=delete(r,x)
inorder(r)
root=delete(r,30)
inorder(r)
root=delete(r,50)
inorder(r)



  