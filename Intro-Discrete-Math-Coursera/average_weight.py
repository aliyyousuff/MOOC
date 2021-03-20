# Compute the average weight of a Hamiltonian cycle in the given graph.

import networkx as nx
from itertools import permutations

def cycle_length2(g, cycle):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()
    w = 0
    cycle += (cycle[0],)
    for i in range(len(cycle)-1):
    #print(cycle1[i], cycle1[i+1])
        w += sum(g[cycle[i]][cycle[i+1]].values())
    return w


import math
def average(g):
    
     n = g.number_of_nodes()
     sum_of_weights = sum(g[i][j]['weight'] for i in range(n) for j in range(i))
     
     return 2*sum_of_weights/(n-1)
    
    



