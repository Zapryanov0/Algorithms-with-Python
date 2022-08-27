from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


edges = int(input())
graph = {}

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(', ')]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, weight))

start_node = int(input())
destination_node = int(input())

max_node = max(graph.keys())

distance = [float('inf')] * (max_node + 1)
parent = [None] * (max_node + 1)

distance[start_node] = 0

priority_queue = PriorityQueue()
priority_queue.put((0, start_node))

while not priority_queue.empty():
    min_distance, node = priority_queue.get()
    if node == destination_node:
        break
    for edge in graph[node]:
        new_distance = min_distance + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = node
            priority_queue.put((new_distance, edge.destination))

if distance[destination_node] == float('inf'):
    print('There is no such path.')
else:
    print(distance[destination_node])

    path = []
    node = destination_node
    while node is not None:
        path.insert(0, node)
        node = parent[node]
    print(*path, sep=' ')
