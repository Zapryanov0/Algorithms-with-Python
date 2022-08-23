def explore_area(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if matrix[row][col] != '-':
        return 0

    matrix[row][col] = 'v'

    result = 1
    result += explore_area(row - 1, col, matrix)
    result += explore_area(row + 1, col, matrix)
    result += explore_area(row, col - 1, matrix)
    result += explore_area(row, col + 1, matrix)

    return result


rows = int(input())
cols = int(input())

matrix = []
for _ in range(rows):
    matrix.append(list(input()))

areas = []
for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col, matrix)
        if size == 0:
            continue
        areas.append((row, col, size))


print(f'Total areas found: {len(areas)}')
areas = sorted(areas, key=lambda a: a[2], reverse=True)
for i in range(0, len(areas)):
    print(f'Area #{i+1} at ({areas[i][0]}, {areas[i][1]}), size: {areas[i][2]}')


# 4
# 9
# ---*---*-
# ---*---*-
# ---*---*-
# ----*-*--