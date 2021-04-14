#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start

# from heapq import heappop, heappush

# class Ugly():
#     def __init__(self):
#         seen = {1}
#         heap = []
#         self.nums = nums = []
#         heappush(heap, 1)

#         for i in range(1690):
#             num = heappop(heap)
#             nums.append(num)

#             for i in [2, 3, 5]:
#                 n_ugly = num * i
#                 if n_ugly not in seen:
#                     seen.add(n_ugly)
#                     heappush(heap, n_ugly)


class Ugly():
    def __init__(self):
        self.nums = nums = [1]
        i2, i3, i5 = 0, 0, 0

        for i in range(1690):
            num = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(num)

            if nums[i2] * 2 == num:
                i2 += 1
            if nums[i3] * 3 == num:
                i3 += 1
            if nums[i5] * 5 == num:
                i5 += 1


class Solution:
    ugly = Ugly()

    def nthUglyNumber(self, n: int) -> int:
        return self.ugly.nums[n - 1]


# @lc code=end
