def recursive_nested_loops(arr, index=0):
    if index >= len(arr):
        print(*arr, sep=' ')
        return

    for number in range(1, len(arr) + 1):
        arr[index] = number
        recursive_nested_loops(arr, index + 1)


arr = [0 for _ in range(int(input()))]
recursive_nested_loops(arr)
