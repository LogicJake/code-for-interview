def build_heap(nums, i, max_len):
    left = i * 2 + 1
    right = i * 2 + 2

    max_index = i

    if left < max_len and nums[left] > nums[i]:
        max_index = left

    if right < max_len and nums[right] > nums[max_index]:
        max_index = right

    if max_index != i:
        nums[max_index], nums[i] = nums[i], nums[max_index]
        build_heap(nums, max_index, max_len)


def heap_sort(nums):
    n = len(nums)

    # 从最后一个非叶结点调整堆
    for i in range(n // 2 - 1, -1, -1):
        build_heap(nums, i, n)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        build_heap(nums, 0, i)


nums = [3, 12, 3, 4, 61, 12]
heap_sort(nums)
print(nums)
