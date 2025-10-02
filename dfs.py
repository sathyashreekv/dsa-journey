def dfs(graph,start,goal,path=[]):
    path=path+[start]
    if start==goal:
        return path
    for node in graph[start]:
        if node not in path:
            new_path=dfs(graph,node,goal,path)
            if new_path:
                return new_path
    return None
def main():
    graph={
        'A':['B','C'],
        'B':['D','E'],
        'C':['F'],
        'D':[],
        'E':['F'],
        'F':[]
    }
    start='A'
    goal='F'
    path=dfs(graph,start,goal)
    if path:
        print(f"Path from {start} to {goal} is: {' -> '.join(path)}")
    else:
        print(f"No path found from {start} to {goal}")
if __name__=="__main__":
    main()