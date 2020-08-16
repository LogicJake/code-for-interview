#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#


# @lc code=start
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int,
                    G: int, H: int) -> int:
        x1 = max(A, E)
        y1 = max(B, F)
        x2 = min(C, G)
        y2 = min(D, H)

        area1 = (C - A) * (D - B)
        area2 = (H - F) * (G - E)

        if x1 <= x2 and y1 <= y2:
            return area1 + area2 - ((x2 - x1) * (y2 - y1))
        else:
            return area1 + area2


# @lc code=end
