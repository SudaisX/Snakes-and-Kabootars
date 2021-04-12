#Imports
import pygame
from dsa import Graph, Stack, Queue
from pprint import pprint
from random import randint

#Player class
class Player():
    def __init__(self):
        pass

    def draw(self):
        pass

#Time class
class Time():
    pass

#Dice class
class Dice():
    def __init__(self):
        pass

    def roll(self):
        pass

#Setting the graph up
graph = Graph()

nodes = [i for i in range(1, 101)]
edges = [(i, i+1, 1) for i in range(1, 100)]

snakes = []
ladders = []

graph.addNodes(nodes)
graph.addEdges(edges, True) #for the basic
graph.addEdges(snakes, True)
graph.addEdges(ladders, True)

#debugging
pprint(graph.displayGraph())