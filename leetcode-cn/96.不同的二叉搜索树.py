#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#


# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(0, i):
                G[i] += G[j] * G[i - j - 1]

        return G[n]


# @lc code=end
