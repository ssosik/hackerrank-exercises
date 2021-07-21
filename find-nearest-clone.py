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
        self.connections = set()
        print(f"Add {self.id} color {color}")

    def connect(self, peer):
        self.connections.add(peer)
        print(f"Connect {self.id} to {peer}")

    def __str__(self):
        return f"<Node {self.id} color {self.color}>"

    def __repr__(self):
        return f"<Node {self.id} color {self.color}>"

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
        self.nodes[frm].connect(self.nodes[to])

    def findNodesOfColor(self, c):
        return [n for n in self.nodes.values() if n.color == c]


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    g = Graph()
    for i, c in enumerate(ids, 1):
        g.addNode(i, c)
    for f, t in zip_longest(graph_from, graph_to):
        g.connect(f, t)

    nodes = g.findNodesOfColor(val)
    print(nodes)

    return 1

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

