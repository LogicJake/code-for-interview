def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        if i != min_index:
            nums[min_index], nums[i] = nums[i], nums[min_index]


nums = [3, 12, 31, 4, 61, 13]
selection_sort(nums)
print(nums)
