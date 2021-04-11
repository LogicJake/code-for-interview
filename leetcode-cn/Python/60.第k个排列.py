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

        k = k - 1

        for i in range(n, 0, -1):
            group_size = 1
            for j in range(i - 1, 0, -1):
                group_size = group_size * j

            group_n = k // group_size

            number = n_list[group_n]
            res += str(number)
            n_list.remove(number)

            k = k % group_size

        return res


# @lc code=end
