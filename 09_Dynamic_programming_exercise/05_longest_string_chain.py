from collections import deque

words = input().split()

size = [0] * len(words)
prev = [None] * len(words)

best_size = 0
best_index = 0

for i in range(len(words)):
    current_word = words[i]
    current_size = 1
    parent = None

    for prev_i in range(i - 1, -1, -1):
        prev_word = words[prev_i]

        if len(prev_word) >= len(current_word):
            continue

        if size[prev_i] + 1 >= current_size:
            current_size = size[prev_i] + 1
            parent = prev_i

    size[i] = current_size
    prev[i] = parent

    if current_size > best_size:
        best_size = current_size
        best_index = i

lis = deque()

index = best_index
while index is not None:
    lis.appendleft(words[index])
    index = prev[index]

print(*lis, sep=' ')
