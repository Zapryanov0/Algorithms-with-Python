def recursive_fibonacci(n):
    if n <= 1:
        return 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


n = int(input())
print(recursive_fibonacci(n))
