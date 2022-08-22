def sum_of_numbers(numbers, index=0):
    if index == len(numbers) - 1:
        return numbers[index]
    return numbers[index] + sum_of_numbers(numbers, index+1)

numbers = [int(num) for num in input().split()]
print(sum_of_numbers(numbers))