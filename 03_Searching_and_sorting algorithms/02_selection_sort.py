def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for current_index in range(i + 1, len(nums)):
            if nums[current_index] < nums[min_index]:
                min_index = current_index
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


nums = [int(num) for num in input().split()]
print(*selection_sort(nums), sep=" ")
