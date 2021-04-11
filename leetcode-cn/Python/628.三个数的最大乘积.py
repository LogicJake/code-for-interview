#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#


# @lc code=start
class Solution:
    def maximumProduct(self, nums):
        a, b, c = float('-inf'), float('-inf'), float('-inf')
        d, e = float('inf'), float('inf')
        for i in range(len(nums)):
            if nums[i] > a:
                a, b, c = nums[i], a, b
            elif nums[i] > b:
                b, c = nums[i], b
            elif nums[i] > c:
                c = nums[i]

            if nums[i] < d:
                d, e = nums[i], d
            elif nums[i] < e:
                e = nums[i]
        return max(a * b * c, a * d * e)


# @lc code=end
