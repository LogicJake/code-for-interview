#
# @lc app=leetcode.cn id=1625 lang=python3
#
# [1625] 执行操作后字典序最小的字符串
#


# @lc code=start
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        mem = set()

        def dfs(ss):
            nonlocal mem
            if ss in mem:
                return
            else:
                mem.add(ss)

            # 累加
            ss1 = list(ss)

            for i in range(1, len(ss1), 2):
                num = int(ss1[i])
                num = (num + a) % 10
                ss1[i] = str(num)
            ss1 = ''.join(ss1)
            dfs(ss1)

            # 轮转
            ss2 = ['0'] * len(ss)

            for i, c in enumerate(ss):
                new_i = (i + b) % len(ss)
                ss2[new_i] = c
            ss2 = ''.join(ss2)
            dfs(ss2)

        dfs(s)

        return min(mem)


# @lc code=end
