from collections import deque

nodes = int(input())
pairs = int(input())

graph = {}
for _ in range(nodes):
    node_str, children_str = input().split(':')
    node = int(node_str)
    children = [int(x) for x in children_str.split()] if children_str else []
    graph[node] = children

for _ in range(pairs):
    source, destination = [int(x) for x in input().split('-')]
    queue = deque([source])
    visited = {}
    for key in graph.keys():
        visited[key] = False
    visited[source] = True

    parent = {}
    for key in graph.keys():
        parent[key] = None

    while queue:
        node = queue.popleft()
        if node == destination:
            break
        for child in graph[node]:
            if visited[child]:
                continue
            queue.append(child)
            visited[child] = True
            parent[child] = node

    if parent[destination] is None:
        print(f'{{{source}, {destination}}} -> -1')
        continue

    node = destination
    size = 0
    while node is not None:
        node = parent[node]
        size += 1

    print(f'{{{source}, {destination}}} -> {size - 1}')
