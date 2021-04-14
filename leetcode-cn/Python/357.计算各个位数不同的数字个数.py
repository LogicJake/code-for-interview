#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 计算各个位数不同的数字个数
#


# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        tag = [0] * 10
        res = 0

        def help(nums, index, n):
            nonlocal res

            if n == 0:
                return

            for i, num in enumerate(nums):
                if not (index == 0 and num == 0) and tag[i] == 0:
                    tag[i] = 1
                    res += 1
                    help(nums, 1, n - 1)
                    tag[i] = 0

        nums = list(range(10))
        help(nums, 0, n)
        return res + 1


# @lc code=end
