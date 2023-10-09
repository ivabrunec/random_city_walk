## main script
import generate_graph
import generate_random_walk

if __name__ == '__main__':
    place = 'Manhattan, New York, USA'  
    graph, nodes, streets = generate_graph.generate_graph(place)
    
    geom_list = generate_random_walk.perform_random_walk(graph, nodes)
