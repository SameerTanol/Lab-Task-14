# Q1 : Implement an algorithm to find the minimum and maximum values stored in a BST.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_minimum_value(root):
    current = root
    while current.left:
        current = current.left
    return current.value

def find_maximum_value(root):
    current = root
    while current.right:
        current = current.right
    return current.value


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)


min_value = find_minimum_value(root)
print("Minimum value in the BST:", min_value)

max_value = find_maximum_value(root)
print("Maximum value in the BST:", max_value)

# Q2 Implement bubble sort algorithm.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr)

print("Sorted array:", arr)

# Q3: Implement the Depth-First Search algorithm for a graph. Test it on a sample graph and print the visited nodes.
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                self.dfs_util(neighbour, visited)

    def dfs(self, start_vertex):
        visited = [False] * (len(self.graph))
        self.dfs_util(start_vertex, visited)

graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print("Depth-First Search traversal:")
graph.dfs(2)

# Q4: Implement the Breadth-First Search algorithm for a graph. Apply BFS to find the shortest path between two nodes in a graph.

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs_shortest_path(self, start_vertex, end_vertex):
        visited = [False] * (len(self.graph))
        queue = deque()
        queue.append((start_vertex, [start_vertex]))

        while queue:
            current_vertex, path = queue.popleft()
            visited[current_vertex] = True

            if current_vertex == end_vertex:
                return path

            for neighbour in self.graph[current_vertex]:
                if not visited[neighbour]:
                    queue.append((neighbour, path + [neighbour]))
                    visited[neighbour] = True

        return None


graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

shortest_path = graph.bfs_shortest_path(2, 3)
if shortest_path:
    print("Shortest path between nodes 2 and 3:", shortest_path)
else:
    print("There is no path between nodes 2 and 3.")
