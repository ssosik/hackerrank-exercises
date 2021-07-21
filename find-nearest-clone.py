#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import zip_longest

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
class Node():
    def __init__(self, _id, color):
        self.id = _id
        self.color = color

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

class Graph():
    def __init__(self):
        self.nodes = dict()

    def addNode(self, _id, color):
        if _id in self.nodes:
            return self.nodes[_id]
        n = Node(_id, color)
        self.nodes[_id] = n
        return n

    def connect(self, frm, to):
        pass

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    g = Graph()
    for i, c in enumerate(ids, 1):
        print(i,c)
        g.addNode(i, c)
    for f, t in zip_longest(graph_from, graph_to):
        print(f,t)
        g.connect(f, t)
    print(1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()

