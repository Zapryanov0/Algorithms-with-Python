def recursive_vector(vector, index=0):
    if index >= len(vector):
        print(*vector, sep="")
        return

    for n in range(2):
        vector[index] = n
        recursive_vector(vector, index + 1)


n = int(input())
vector = [0] * n
recursive_vector(vector)
