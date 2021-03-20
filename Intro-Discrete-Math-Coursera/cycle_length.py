# Implement a function which takes a graph and a list of vertices in a Hamiltonian cycle, 
# and returns the weight of this cycle.

import networkx as nx


def cycle_length(g, cycle):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()
    
    # Write your code here.
    w = 0
    cycle.append(cycle[0])
    
    for i in range(len(cycle)-1):
        w += sum(g[cycle[i]][cycle[i+1]].values())
    return w

