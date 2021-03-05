def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


nums = [3, 12, 31, 4, 61, 13]
bubble_sort(nums)
print(nums)
