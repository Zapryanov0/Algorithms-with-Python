def binary_search(numbers, target):

    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = numbers[mid_idx]
        if mid_el == target:
            return mid_idx
        if mid_el < target:
            left = mid_idx + 1
        else:
            right = mid_idx - 1
    return -1


# def binary_search(nums, target):
#     index_of_half = 0
#     while True:
#         mid = nums[int(len(nums) / 2)]
#         if mid > target:
#             nums = nums[0:int(len(nums) / 2)]
#         elif mid < target:
#             index_of_half += int(len(nums) / 2)
#             nums = nums[int(len(nums) / 2):]
#         else:
#             return int(len(nums) / 2) + index_of_half


nums = [int(num) for num in input().split()]
target = int(input())
print(binary_search(nums, target))
