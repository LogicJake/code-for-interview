#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [1]
        for _ in range(rowIndex):
            arr.append(1)
            for j in range(len(arr) - 2, 0, -1):
                arr[j] += arr[j - 1]
        return arr


# @lc code=end
