#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] 水壶问题
#


# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]

        seen = set()

        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or (remain_x + remain_y) == z:
                return True

            if (remain_x, remain_y) in seen:
                continue
            seen.add((remain_x, remain_y))

            stack.append((0, remain_y))
            stack.append((remain_x, 0))

            stack.append((x, remain_y))
            stack.append((remain_x, y))

            stack.append((remain_x - min(y - remain_y, remain_x),
                          remain_y + min(y - remain_y, remain_x)))

            stack.append((remain_x + min(x - remain_x, remain_y),
                          remain_y - min(x - remain_x, remain_y)))
        return False


# @lc code=end
