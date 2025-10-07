class WeightedGraph:
    def __init__(self):
        self.adj_list={}
    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]={}
            return True
        return False
    def add_edge(self,vertex1,vertex2,weight,directed=False):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1][vertex2]=weight
            if not directed:
                self.adj_list[vertex2][vertex1]=weight
                return True
        return False
    
    def remove_edge(self,vertex1,vertex2,weight,directed=False):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].pop(vertex2, None)
            if not directed:
                self.adj_list[vertex2].pop(vertex1, None)
            return True
        return False
    def remove_vertex(self,vertex):
        if vertex in self.adj_list:
            del self.adj_list[vertex]
            for v in self.adj_list:
                    self.adj_list[v].pop(vertex,None)
            return True
        return False
    
    def get_friends(self,vertex):
        return self.adj_list.get(vertex,{})
    def __str__(self):
        return str(self.adj_list)
    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")
    
if __name__=="__main__":
    wg = WeightedGraph()
    wg.add_vertex('A')
    wg.add_vertex('B')
    wg.add_vertex('C')

    wg.add_edge('A', 'B', 5)  # Edge from A to B with weight 5
    wg.add_edge('A', 'C', 10) # Edge from A to C with weight 10
    wg.add_edge('B', 'C', 3)
    wg.print_graph()
    wg.remove_edge('A', 'B', 5)
    wg.print_graph()