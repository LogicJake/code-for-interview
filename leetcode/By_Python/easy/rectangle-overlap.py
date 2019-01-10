# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-10 12:59:29
# @Last Modified time: 2019-01-10 16:46:33


class Solution:

    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top

if __name__ == '__main__':
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    solution = Solution()
    res = solution.isRectangleOverlap(rec1, rec2)
    print(res)
