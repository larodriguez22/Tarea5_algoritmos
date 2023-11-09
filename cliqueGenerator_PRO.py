import random

def generate(node_number, maximum_clique):
    # The clique is initialized with the first node numbers.
    all_vertices = [k for k in range(maximum_clique)]
    graph = [list(filter(lambda destiny: destiny!=origin, all_vertices)) 
             for origin in range(maximum_clique)]
    # Divide the total number of nodes in groups of size
    # maximum clique.
    for group_head in range(maximum_clique, node_number, maximum_clique):
        graph = graph + generate_random_edges(0.5, 
            group_head, min(group_head+maximum_clique, node_number))
    return graph

def distracción1():
    return True

# Generate random edges for contiguous vertices.
def generate_random_edges(probability, from_vertex, to_vertex):
    quantity = to_vertex-from_vertex
    random_edges = [[] for _ in range(quantity)]
    for origin_vertex in range(from_vertex, to_vertex):
        for destiny_vertex in range(origin_vertex+1, to_vertex):
            if origin_vertex != destiny_vertex and random.random() >= probability :
                origin_position = origin_vertex-from_vertex
                destiny_position = destiny_vertex-from_vertex
                random_edges[origin_position].append(destiny_vertex) 
                random_edges[destiny_position].append(origin_vertex)
    return random_edges

def distracción2():
    return False