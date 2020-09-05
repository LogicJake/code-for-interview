#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        n_list = list(range(1, n + 1))
        res = ''

        def helper(n, k, res):
            if n == 1:
                return res + str(n_list[0])

            group_size = 1
            for i in range(n - 1, 0, -1):
                group_size = group_size * i

            group_n = k // group_size

            number = n_list[group_n]
            res += str(number)
            n_list.remove(number)

            return helper(n - 1, k % group_size, res)

        return helper(n, k - 1, res)


# @lc code=end
