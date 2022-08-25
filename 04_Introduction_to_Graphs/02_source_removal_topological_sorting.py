def find_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result


def find_node_without_dependencies(dependencies):
    for node, dep_count in dependencies.items():
        if dep_count == 0:
            return node
    return None


nodes = int(input())

graph = {}
for _ in range(nodes):
    line_parts = input().split('->')
    node = line_parts[0].strip()
    children = line_parts[1].strip().split(', ') if line_parts[1] else []
    graph[node] = children

dependencies = find_dependencies(graph)
has_cycles = False
result = []

while dependencies:
    node_to_remove = find_node_without_dependencies(dependencies)
    if node_to_remove is None:
        has_cycles = True
        break
    dependencies.pop(node_to_remove)
    result.append(node_to_remove)
    for child in graph[node_to_remove]:
        dependencies[child] -= 1


if has_cycles:
    print('Invalid topological sorting')
else:
    print(f"Topological sorting: {', '.join(result)}")


# Input
# 6
# A -> B, C
# B -> D, E
# C -> F
# D -> C, F
# E -> D
# F ->

# Output
# Topological sorting: A, B, E, D, C, F
