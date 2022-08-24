def bubble_sort(nums):
    counter = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for index in range(1, len(nums) - counter):
            if nums[index] < nums[index - 1]:
                nums[index], nums[index - 1] = nums[index - 1], nums[index]
                is_sorted = False
        counter += 1
    return nums


# def bubble_sort(nums):
#     for i in range(len(nums)):
#         for j in range(1, len(nums) - i):
#             if nums[j - 1] > nums[j]:
#                 nums[j], nums[j - 1] = nums[j - 1], nums[j]
#     return nums


nums = [int(num) for num in input().split()]
print(*bubble_sort(nums), sep=" ")
