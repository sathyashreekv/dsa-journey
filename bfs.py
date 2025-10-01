class TreeNode:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
from collections import deque
def bfs(root):
    queue=deque()
    result=[]
    if not root:
        return result
    queue.append(root)
    while queue:
        if len(queue)==0:
            break
        node=queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
def main():
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(4)
    root.left.right=TreeNode(5)
    root.right.left=TreeNode(6)
    root.right.right=TreeNode(7)
    print("BFS Traversal of the tree is:",bfs(root))
if __name__=="__main__":
    main()
        
