import osmnx as ox

def generate_graph(place):
    graph = ox.graph_from_place(place, network_type='drive')
    nodes, streets = ox.graph_to_gdfs(graph)
    streets = streets.reset_index()
    nodes = nodes.reset_index()
    return graph, nodes, streets
