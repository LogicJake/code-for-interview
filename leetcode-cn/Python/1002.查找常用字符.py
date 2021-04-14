#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#

# @lc code=start
from typing import List
import string


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        cnt = {}

        for i in string.ascii_lowercase:
            cnt[i] = 9999999

        for a in A:
            tmp = {}
            for i in string.ascii_lowercase:
                tmp[i] = 0
            for c in list(a):
                tmp[c] += 1

            for k in tmp:
                cnt[k] = min(cnt[k], tmp[k])

        ans = []
        for i in string.ascii_lowercase:
            if cnt[i] != 0:
                ans.extend([i] * cnt[i])

        return ans


# @lc code=end
