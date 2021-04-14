#
# @lc app=leetcode.cn id=842 lang=python3
#
# [842] 将数组拆分成斐波那契序列
#

# @lc code=start
from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans = []
        m = len(S)

        def help(index):
            if index == m:
                return len(ans) >= 3

            cur = 0
            for i in range(index, m):
                # 忽略以 0 开头的数字
                if i > index and S[index] == '0':
                    break

                cur = cur * 10 + ord(S[i]) - ord('0')
                if cur > 2**31 - 1:
                    break

                if len(ans) < 2 or cur == ans[-1] + ans[-2]:
                    ans.append(cur)
                    if help(i + 1):
                        return True
                    ans.pop()

            return False

        help(0)
        return ans


# @lc code=end
