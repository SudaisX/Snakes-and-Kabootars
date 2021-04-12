from pprint import pprint
from dsa import Graph, Stack, Queue

graph = Graph()
graph.addNodes([i for i in range(101)])


pprint(graph.displayGraph())