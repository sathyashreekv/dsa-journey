import collections
def bfs(graph,start):
    visited=set()
    queue=collections.deque()
    queue.append(start)
    visited.add(start)
    while queue:
        current_node=queue.popleft()
        print(current_node,end=" ")
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

my_graph={
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','E'],
    'D':['B','F'], 
    'E':['C','F'],
    'F':['D','E']
}
print("BFS Traversal starting from node A:")
bfs(my_graph,'A')