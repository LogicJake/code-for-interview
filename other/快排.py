def quick_sort(nums, left, right):
    if left >= right:
        return

    privot = nums[left]

    i = left
    j = right

    while i < j:
        while i < j and nums[j] >= privot:
            j -= 1
        nums[i] = nums[j]

        while i < j and nums[i] <= privot:
            i += 1
        nums[j] = nums[i]

    nums[i] = privot
    quick_sort(nums, left, i - 1)
    quick_sort(nums, i + 1, right)


nums = [3, 12, 5, 4, 61, 13]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
