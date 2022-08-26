def dfs(node, graph, visited, component):
    if visited[node]:
        return
    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, component)
    component.append(node)


nodes = int(input())
graph = []

for node in range(nodes):
    line = input()
    children = [] if line == '' else [int(child) for child in line.split()]
    graph.append(children)

visited = [False] * nodes

for node in range(nodes):
    if visited[node]:
        continue
    component = []
    dfs(node, graph, visited, component)
    print(f"Connected component: {' '.join(map(str, component))}")

# Input
# 9
# 3 6
# 3 4 5 6
# 8
# 0 1 5
# 1 6
# 1 3
# 0 1 4
#
# 2

# Output
# Connected component: 6 4 5 1 3 0
# Connected component: 8 2
# Connected component: 7
