import numpy as np 
from heapq import heappush,heappop

class abstract_graph:
    def __init__(self,_edges):
        self.edges=_edges
        self.nodes={u for u,v in self.edges} | {v for u,v in self.edges}

    def adjacency_matrix(self):
        pass

    def adjacency_list(self)
        pass


