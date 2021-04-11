#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            mem[key].append(s)

        return list(mem.values())


# @lc code=end
