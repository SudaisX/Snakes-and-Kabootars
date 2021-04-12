from pprint import pprint
from dsa import Graph, Stack, Queue

graph = Graph()

graph.addNodes([i for i in range(101)])
graph.addEdges([(i, i+1, 1) for i in range(100)], True)

pprint(graph.displayGraph())