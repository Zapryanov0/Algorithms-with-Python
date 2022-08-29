def calc_fibonacci(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    result = calc_fibonacci(n - 1, memo) + calc_fibonacci(n - 2, memo)
    memo[n] = result
    return result


n = int(input())
print(calc_fibonacci(n, {}))
