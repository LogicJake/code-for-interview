def quick_sort(nums):
    privot = nums[0]

    left = 0
    right = len(nums) - 1

    while left < right:
        while left < right and nums[right] > 0:
            right -= 1

        nums[left] = nums[right]

        while left < right and nums[left] < 0:
            left += 1

        nums[right] = nums[left]

    nums[left] = privot


nums = [-3, 12, -5, 4, -61, 13]
quick_sort(nums)
print(nums)
