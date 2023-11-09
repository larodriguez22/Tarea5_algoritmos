import random
import networkx as nx
import matplotlib.pyplot as plt

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

def generate2(node_number, maximum_clique):
    # The clique is initialized with the first node numbers.
    all_vertices = [k for k in range(maximum_clique)]
    graph = {origin: list(filter(lambda destiny: destiny!=origin, all_vertices)) 
             for origin in range(maximum_clique)}
    # Divide the total number of nodes in groups of size
    # maximum clique.
    for group_head in range(maximum_clique, node_number, maximum_clique):
        graph.update(generate_random_edges2(0.5, 
            group_head, min(group_head+maximum_clique, node_number)))
    return graph
    
# Generate random edges for contiguous vertices.
def generate_random_edges2(probability, from_vertex, to_vertex):
    edges = []
    for origin_vertex in range(from_vertex, to_vertex):
        for destiny_vertex in range(origin_vertex+1, to_vertex):
            if origin_vertex != destiny_vertex and random.random() >= probability:
                edges.append((origin_vertex, destiny_vertex))
    return {origin: [destiny for (o, destiny) in edges if o == origin] for origin in range(from_vertex, to_vertex)}

# Draw the graph
def draw_graph(graph):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)  # You can choose a different layout if needed
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, font_color='black', edge_color='gray', linewidths=0.5)
    plt.show()
