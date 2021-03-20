# Implement the brute force algorithm for the Traveling Salesman Problem. The algorithm should check all the permutations of the vertices
# and return the minimum weight of a cycle visiting each vertex exactly once.

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



def all_permutations(g):
    
    p = list(permutations(list(g.nodes())))
    d = {}
    for i in p:
        d[i] = cycle_length2(g, i)
    return d[min(d, key=d.get)]
    
    


