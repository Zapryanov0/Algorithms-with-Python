def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


nodes_count = int(input())
edges_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes_count)]

edges = []
for _ in range(edges_count):
    first_node, second_node = [int(x) for x in input().split(" - ")]
    graph[first_node].append(second_node)
    graph[second_node].append(first_node)
    edges.append((min(first_node, second_node), max(first_node, second_node)))

print(f'Important streets:')
for first_node, second_node in edges:
    graph[first_node].remove(second_node)
    graph[second_node].remove(first_node)

    visited = [False] * nodes_count
    dfs(0, graph, visited)

    if not all(visited):
        print(first_node, second_node)

    graph[first_node].append(second_node)
    graph[second_node].append(first_node)
