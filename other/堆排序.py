def build_heap(nums, i, max_len):
    left_index = i * 2 + 1
    right_index = i * 2 + 2

    max_index = i
    if left_index < max_len and nums[left_index] > nums[max_index]:
        max_index = left_index

    if right_index < max_len and nums[right_index] > nums[max_index]:
        max_index = right_index

    if max_index != i:
        nums[max_index], nums[i] = nums[i], nums[max_index]

        build_heap(nums, max_index, max_len)


def heap_sort(nums):
    n = len(nums)

    for i in range(n // 2 - 1, -1, -1):
        build_heap(nums, i, n)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        build_heap(nums, 0, i)


nums = [3, 12, 31, 4, 61, 13]
heap_sort(nums)
print(nums)
