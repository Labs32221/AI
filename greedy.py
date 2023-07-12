# A Node class for GBFS Pathfinding
class Node:
    def __init__(self, v, weight):
        self.v = v
        self.weight = weight

# pathNode class will help to store
# the path from src to dest.
class pathNode:
    def __init__(self, node, parent):
        self.node = node
        self.parent = parent

# Function to add edge in the graph.
def addEdge(u, v, weight):
    # Add edge u -> v with weight weight.
    adj[u].append(Node(v, weight))

# Greedy best first search algorithm function
def GBFS(h, V, src, dest):
    """
    This function returns a list of
    integers that denote the shortest
    path found using the GBFS algorithm.
    If no path exists from src to dest, we will return an empty list.
    """
    # Initializing openList and closeList.
    openList = []
    closeList = []

    # Inserting src in openList.
    openList.append(pathNode(src, None))

    # Iterating while the openList
    # is not empty.
    while openList:

        currentNode = openList[0]
        currentIndex = 0
        # Finding the node with the least 'h' value
        for i in range(len(openList)):
            if h[openList[i].node] < h[currentNode.node]:
                currentNode = openList[i]
                currentIndex = i

        # Removing the currentNode from
        # the openList and adding it in
        # the closeList.
        openList.pop(currentIndex)
        closeList.append(currentNode)

        # If we have reached the destination node.
        if currentNode.node == dest:
            # Initializing the 'path' list.
            path = []
            cur = currentNode

            # Adding all the nodes in the
            # path list through which we have
            # reached to dest.
            while cur:
                path.append(cur.node)
                cur = cur.parent

            # Reversing the path, because
            # currently it denotes path
            # from dest to src.
            path.reverse()
            return path

        # Iterating over adjacents of 'currentNode'
        # and adding them to openList if
        # they are neither in openList or closeList.
        for node in adj[currentNode.node]:
            if node.v not in [x.node for x in openList] and node.v not in [x.node for x in closeList]:
                openList.append(pathNode(node.v, currentNode))

    return []

# Driver Code

# The total number of vertices.
V = int(input("Enter the number of vertices: "))

# Initializing the adjacency list
adj = [[] for _ in range(V)]

# Getting input for edges and weights
print("Enter the edges (u v weight), one per line (press enter to stop):")
while True:
    edge = input().split()
    if len(edge) != 3:
        break
    u, v, weight = map(int, edge)
    addEdge(u, v, weight)

# Getting user input for the source and destination nodes.
src = int(input("Enter the source node: "))
dest = int(input("Enter the destination node: "))

# Getting the heuristic values for each node.
h = []
for i in range(V):
    h_value = int(input("Enter the heuristic value for node " + str(i) + ": "))
    h.append(h_value)

# Finding the shortest path using GBFS.
path = GBFS(h, V, src, dest)

# Printing the shortest path if it exists.
if path:
    print("Shortest path:", " -> ".join(str(node) for node in path))
else:
    print("No path found from source to destination.")


Enter the number of vertices: 10
Enter the edges (u v weight), one per line (press enter to stop):
0 1 3
0 2 2
1 3 4
1 4 1
2 5 3
2 6 1
5 7 5
6 8 2
6 9 3

Enter the source node: 0
Enter the destination node: 7
Enter the heuristic value for node 0: 12
Enter the heuristic value for node 1: 4
Enter the heuristic value for node 2: 7
Enter the heuristic value for node 3: 3
Enter the heuristic value for node 4: 8
Enter the heuristic value for node 5: 2
Enter the heuristic value for node 6: 4
Enter the heuristic value for node 7: 9
Enter the heuristic value for node 8: 13
Enter the heuristic value for node 9: 0
Shortest path: 0 -> 2 -> 5 -> 7
