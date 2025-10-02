def dfs_recursive(graph,node,visited=None):
    if visited is None:
        visited=set()
    if node not in visited:
        visited.add(node)
        print(node,end=" ")
        for neighbor in graph[node]:
            dfs_recursive(graph,neighbor,visited)
    return visited
def dfs_iterative(graph,start):
    visited=set()
    stack=[start]
    while stack:
        node=stack.pop()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            stack.extend(graph[node]-visited)
    return visited
graph={
    'A':{'B','C'},
    'B':{'D','E'},
    'C':{'F'}, 
    'D':set(),
    'E':{'F'},
    'F':set()
}
dfs_recursive(graph,'A')
print()
dfs_iterative(graph,'A')

