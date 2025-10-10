from collections import deque

def findCircularCity(isConnected: list[list[int]]) -> int:
    n=len(isConnected)
    visited=set()
    provinces=0
    for i in range(n):
        if i not in visited:
            provinces+=1
            queue=deque([i])
            while queue:
                city=queue.popleft()
                visited.add(city)
                for neighbor in range(n):
                    if isConnected[city][neighbor]==1 and neighbor not in visited:
                        queue.append(neighbor)
    return provinces

if __name__=="__main__":
    matrix=[
        [1,1,0],
        [1,1,0],
        [0,0,1]
    ]
    print(f"Number of  proviences(BFS) :{findCircularCity(matrix)}")