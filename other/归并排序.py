def merge_sort(nums, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)

    tmp = list(nums)

    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if tmp[i] < tmp[j]:
            nums[k] = tmp[i]
            k += 1
            i += 1
        else:
            nums[k] = tmp[j]
            k += 1
            j += 1

    while i <= mid:
        nums[k] = tmp[i]
        k += 1
        i += 1

    while j <= right:
        nums[k] = tmp[j]
        k += 1
        j += 1


nums = [3, 12, 31, 4, 61, 13]
merge_sort(nums, 0, len(nums) - 1)
print(nums)
