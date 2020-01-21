#BFS with recursive solution

class Graph:
    
    def __init__(self):
        self.graph={}
        
    def add_edge(self,v1,v2):
        if v1 in self.graph.keys():
            self.graph[v1]+=[v2]
        else:
            self.graph[v1]=[v2]
       
    def add_vertice(self,v):
        self.graph[v]=[]
                
    def search_level(self, level):
        new_level=[]
        for vertice in level:
            print(vertice, end=' ')
            new_level+=self.graph[vertice]
        if new_level:
            self.search_level(new_level)
                     
    def BFS(self,vertice):
        self.search_level([vertice])
                
        
g=Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_vertice(4)
g.add_edge(1,4)
g.add_edge(2,5)
g.add_vertice(5)
g.add_edge(2,6)
g.add_vertice(6)
g.add_edge(3,7)
g.add_vertice(7)
g.BFS(0)

        
        
            
