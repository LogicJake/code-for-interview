def merge_sort(nums, left, right):
    if left < right:
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
                i += 1
            else:
                nums[k] = tmp[j]
                j += 1

            k += 1

        while i <= mid:
            nums[k] = tmp[i]
            i += 1
            k += 1

        while j <= right:
            nums[k] = tmp[j]
            j += 1
            k += 1


nums = [3, 12, 3, 4, 61, 12]
merge_sort(nums, 0, len(nums) - 1)
print(nums)
