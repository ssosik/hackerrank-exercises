#!/bin/python3

# https://www.hackerrank.com/challenges/matrix

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
    def __init__(self, _id, has_machine=False):
        self.id = _id
        self.has_machine = has_machine
        self.connections = set()
        print(f"Add {self.id} has_machine {has_machine}")

    def connect(self, peer):
        self.connections.add(peer)
        peer.connections.add(self)
        print(f"Connect {self.id} to {peer}")

    def set_machine(self, has_machine=True):
        self.has_machine = has_machine

    def __str__(self):
        return f"<Node {self.id} has_machine {self.has_machine}>"

    def __repr__(self):
        return f"<Node {self.id} has_machine {self.has_machine}>"

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def traverse(self, depth=0, prev=None):
        depth += 1
        for p in self.connections:
            print(f"From {self} Testing peer {p} has_machine {has_machine}")
            if prev is not None and p == prev:
                print(f"p {p} Prev {prev}")
                continue # Don't count where we just were
            #if p.color == color:
            #    print(f"Found color {color} on {p} prev {prev}")
            #    return depth
        for p in self.connections:
            if prev is not None and p == prev:
                print(f"traverse p {p} Prev {prev}")
                continue # Don't count where we just were
            print(f"Traverse from {self} to {p} depth {depth}")
            v = p.traverse(depth, self)
            if v is not None:
                return v
        return None

class Graph():
    def __init__(self):
        self.nodes = dict()
        self.edges = dict()

    def addNode(self, _id, has_machine):
        if _id in self.nodes:
            return self.nodes[_id]
        n = Node(_id, has_machine)
        self.nodes[_id] = n
        return n

    def set_machine(self, _id, has_machine=True):
        self.nodes[_id].set_machine(has_machine)

    def connect(self, frm, to):
        self.nodes[frm].connect(self.nodes[to])

    def findNodesWithMachines(self, c):
        return [n for n in self.nodes.values() if n.has_machine]

def minTime(roads, machines):
    g = Graph()
    for i, c in enumerate(ids, 1):
        g.addNode(i, c)
    for f, t in zip_longest(graph_from, graph_to):
        g.connect(f, t)

    nodes = g.findNodesOfColor(val)
    if len(nodes) < 2:
        return -1
    vals = []
    for n in nodes:
        c = n.traverse(val)
        if c is not None:
            vals.append(c)
        print(f"Walk from {n} took {c}")
    print(nodes)

    if len(vals) == 0:
        return -1
    return min(vals)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = []

    for _ in range(k):
        machines_item = int(input().strip())
        machines.append(machines_item)

    result = minTime(roads, machines)

    fptr.write(str(result) + '\n')

    fptr.close()

