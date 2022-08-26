def dfs(parent, row, col, matrix, visited_matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    if visited_matrix[row][col]:
        return
    if matrix[row][col] != parent:
        return

    visited_matrix[row][col] = True
    dfs(parent, row - 1, col, matrix, visited_matrix)
    dfs(parent, row + 1, col, matrix, visited_matrix)
    dfs(parent, row, col - 1, matrix, visited_matrix)
    dfs(parent, row, col + 1, matrix, visited_matrix)


rows = int(input())
cols = int(input())

matrix = []
visited_matrix = []
for _ in range(rows):
    matrix.append(list(input()))
    visited_matrix.append([False] * cols)

areas = {}
total_areas = 0
for row in range(rows):
    for col in range(cols):
        if visited_matrix[row][col]:
            continue
        parent = matrix[row][col]
        dfs(parent, row, col, matrix, visited_matrix)
        if parent not in areas:
            areas[parent] = 1
        else:
            areas[parent] += 1
        total_areas += 1

print(f'Areas: {total_areas}')
for area, size in sorted(areas.items()):
    print(f"Letter '{area}' -> {size}")
