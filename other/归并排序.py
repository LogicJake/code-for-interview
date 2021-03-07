def merge_sort(nums, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(nums, left, mid)
        merge_sort(nums, mid + 1, right)

        i = left
        j = mid + 1
        k = left
        tmp = list(nums)

        while i < mid + 1 and j < right + 1:
            if tmp[i] < tmp[j]:
                nums[k] = tmp[i]
                i += 1
            else:
                nums[k] = tmp[j]
                j += 1

            k += 1

        while i < mid + 1:
            nums[k] = tmp[i]
            i += 1
            k += 1

        while j < right + 1:
            nums[k] = tmp[j]
            j += 1
            k += 1


nums = [3, 12, 31, 4, 61, 13]
merge_sort(nums, 0, len(nums) - 1)
print(nums)
