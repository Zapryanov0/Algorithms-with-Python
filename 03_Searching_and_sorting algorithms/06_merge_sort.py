def merge_arrays(left, right):
    result = [None] * (len(left) + len(right))
    left_index = 0
    right_index = 0
    result_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result[result_index] = left[left_index]
            left_index += 1
        else:
            result[result_index] = right[right_index]
            right_index += 1
        result_index += 1

    while left_index < len(left):
        result[result_index] = left[left_index]
        left_index += 1
        result_index += 1

    while right_index < len(right):
        result[result_index] = right[right_index]
        right_index += 1
        result_index += 1

    return result


def merge_sort(nums):
    if len(nums) == 1:
        return nums

    mid_index = len(nums) // 2
    left = nums[:mid_index]
    right = nums[mid_index:]

    return merge_arrays(merge_sort(left), merge_sort(right))


nums = [int(num) for num in input().split()]
print(*merge_sort(nums), sep=' ')
