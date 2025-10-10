class Graph:
    def __init__(self):
        self.adjacency_list={}
    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex]=set()
            return True
        return False
    def add_edge(self,vertex1,vertex2,directed=False):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].add(vertex2)
            if not directed:
                self.adjacency_list[vertex2].add(vertex1)
                return True
        return False
    def remove_edge(self,vertex1,vertex2,directed=False):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].discard(vertex2)
            if not directed:
                self.adjacency_list[vertex2].discard(vertex1)
            return True
        return False
    def remove_vertex(self,vertex):
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
            for v in self.adjacency_list:
                    self.adjacency_list[v].discard(vertex)
            return True
        return False
    def get_friends(self,vertex):
        return self.adjacency_list.get(vertex,set())
    def __str__(self):
        return str(self.adjacency_list)
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(f"{vertex} -> {self.adjacency_list[vertex]}")

if __name__=="__main__":
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')

    g.add_edge('A', 'B')  # Edge from A to B
    g.add_edge('A', 'C') # Edge from A to C
    g.add_edge('B', 'C')
    g.print_graph()
    g.remove_edge('A', 'B')
    g.print_graph()