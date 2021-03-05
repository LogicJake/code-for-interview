def selection_sort(nums):
    n = len(nums)
    for i in range(1, n):
        value = nums[i]
        p = i

        while p > 0 and nums[p - 1] > value:
            nums[p] = nums[p - 1]
            p -= 1

        nums[p] = value


nums = [3, 12, 31, 4, 61, 13]
selection_sort(nums)
print(nums)
