"""Graph-related stuff"""
from queue import Queue


def breadth_first_traversal(start, graph, callback=None):
    """Performs a breadth-first traversal of a graph using the following
    algorithm

    for each vertex v in the graph
        if v is not visited
            add v to the queue // start bf search at v

    Mark v as visited
    While the queue is not empty
        remove vertex u from the queue
        retrieve the vertices adjacent to u
        for each vertex w that is adjacent to u
            add w to the queue
            mark w as visited

    Args:
        start:
            The starting node
        graph:
            The graph to traverse. A networkx graph instance
        callback:
            A callback function to be called on each visited node
    """
    # process the starting node
    if callback is not None:
        callback(start)

    node_queue = Queue()
    node_queue.put(start)
    visited = dict()

    for node in graph.nodes():
        visited[node] = False

    visited[start] = True

    while not node_queue.empty():
        node = node_queue.get()

        for neighbor in graph.neighbors(node):
            if not visited[neighbor]:
                callback(neighbor)
                visited[neighbor] = True
                node_queue.put(neighbor)

