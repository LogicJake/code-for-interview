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
        ans_dict = defaultdict(list)

        for s in strs:
            tmp = ''.join(sorted(s))
            ans_dict[tmp].append(s)

        return list(ans_dict.values())


# @lc code=end
