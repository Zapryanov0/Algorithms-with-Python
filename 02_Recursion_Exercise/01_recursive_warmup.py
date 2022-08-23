def recursive_reverse_array(arr, index):
    if index <= 0:
        return []
    return [arr.pop()] + recursive_reverse_array(arr, index - 1)


arr = [int(n) for n in input().split()]
print(*recursive_reverse_array(arr, len(arr)), sep=' ')
