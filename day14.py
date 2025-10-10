import collections

def findCircleNum_bfs(isConnected):
    """
    Solves the Number of Provinces problem using BFS.
    """
    n = len(isConnected)
    visited = set()
    number_of_provinces = 0

    # Loop through all cities
    for i in range(n):
        # If we find a city that has not been visited, it's a new province.
        if i not in visited:
            number_of_provinces += 1
            
            # Now, find all cities in this province using BFS
            queue = collections.deque([i])
            visited.add(i)
            
            while queue:
                current_city = queue.popleft()
                
                # Check all other cities to see if they are connected
                for neighbor in range(n):
                    # If there's a connection and we haven't visited the neighbor
                    if isConnected[current_city][neighbor] == 1 and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        
    return number_of_provinces

# Example Usage:
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(f"Number of provinces (BFS): {findCircleNum_bfs(isConnected)}") # Output: 2

isConnected2 = [[1,0,0],[0,1,0],[0,0,1]]
print(f"Number of provinces (BFS): {findCircleNum_bfs(isConnected2)}") # Output: 3
