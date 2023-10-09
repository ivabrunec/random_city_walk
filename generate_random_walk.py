import random
import osmnx as ox

def perform_random_walk(graph, nodes):
    geom_list = []
    node_id = random.choice(nodes['osmid'])
    node_coords = nodes[nodes['osmid'] == node_id]['geometry']

    for i in range(100):
        neighbors = list(graph.neighbors(node_id))
        valid_neighbors = [neighbor for neighbor in neighbors if 'geometry' in graph[node_id][neighbor][0]]

        if len(valid_neighbors) == 0:
            break

        random_neighbor = random.choice(valid_neighbors)

        # get the edge between the specified node and the randomly selected neighbor
        edge = graph[node_id][random_neighbor][0]
        geom_list.append(edge['geometry'])

        # save selected node as the node id for the next loop iteration
        node_id = random_neighbor

    print(node_id)
    return geom_list
