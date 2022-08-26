def dfs(node, graph, visited, cycles):
    if node in cycles:
        raise Exception
    if node in visited:
        return
    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycles)
    cycles.remove(node)


graph = {}
edge = input()
while edge != 'End':
    parent, child = edge.split('-')
    if parent not in graph:
        graph[parent] = []
    if child not in graph:
        graph[child] = []
    graph[parent].append(child)

    edge = input()

visited = set()
try:
    for node in graph:
        dfs(node, graph, visited, set())
    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')
