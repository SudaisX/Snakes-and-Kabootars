#Imports
import pygame
from pprint import pprint
from random import randint
from dsa import Graph, Stack, Queue

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

graph.addNodes([i for i in range(101)])
graph.addEdges([(i, i+1, 1) for i in range(100)], True)

#debugging
pprint(graph.displayGraph())