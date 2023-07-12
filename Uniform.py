#c.	Uniform Cost Search
from collections import defaultdict
from queue import PriorityQueue
class Graph:
    def __init__(self, directed):
        """Parametrized constructor of class Graph
        which takes True if Graph is directed otherwise it takes False"""
        self.graph =  defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight):
        """Add Edges between two nodes along
        with weight as Algorithm is of UCS"""
        if self.directed:
            value = (weight, v)
            self.graph[u].append(value)
        else:
            value = (weight, v)
            self.graph[u].append(value)
            value = (weight, u)
            self.graph[v].append(value)

    def ucs(self, current_node, goal_node):
        """It takes starting node and
        goal node as parameters then it returns
        a path using Uniform Cost Search Algorithm"""
        visited = []
        queue = PriorityQueue()
        queue.put((0, current_node))

        while not queue.empty():
            item = queue.get()
            current_node =  item[1]

            if current_node == goal_node:
                print(current_node, end = " ")
                queue.queue.clear()
            else:
                if current_node in visited:
                    continue

                print(current_node, end = " ")
                visited.append(current_node)

                for neighbour in self.graph[current_node]:
                        queue.put((neighbour[0], neighbour[1]))

g = Graph(False)
g.graph =  defaultdict(list)
g.add_edge('S', '1', 2)
g.add_edge('S', '3', 5)
g.add_edge('1', '2', 4)
g.add_edge('5', '2', 6)
g.add_edge('4', '5', 3)
g.add_edge('3', '4', 2)
g.add_edge('3', '1', 5)
g.add_edge('1', 'G', 1)
g.add_edge('3', 'G', 6)
g.add_edge('G', '4', 7)
g.add_edge('5', 'G', 3)
g.add_edge('4', '2', 4)
print(g.graph)
g.ucs('S', 'G')