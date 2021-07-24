# 一个小组有n名成员，每个成员都有一个非负整数得分。若小组成员中得分最高的前k人得分都不低于k，且其他成员的得分都不超过k，则该小组成绩为k。输入小组n名成员的得分，求小组成绩k。例如得分为5, 2, 7, 11, 8, 6, 5, 1，得分最高的前5人得分为11, 8, 7, 6, 5，其他3人得分为5, 2, 1，因此该小组得分为5。


def quick_sort(nums, left, right, len):
    p = left
    q = right

    privot = nums[left]

    while p < q:
        while p < q and nums[q] >= privot:
            q -= 1
        nums[p] = nums[q]

        while p < q and nums[p] <= privot:
            p += 1

        nums[q] = nums[p]

    nums[p] = privot
    k = nums[p]
    num_ = len - p
    if num_ == k:
        return k
    elif num_ > k:
        return quick_sort(nums, p + 1, right, len)
    else:
        return quick_sort(nums, left, p - 1, len)


def findK(nums):
    return quick_sort(nums, 0, len(nums) - 1, len(nums))


nums = [2, 5, 7, 11, 8, 6, 5, 1]
ans = findK(nums)
print(ans)
