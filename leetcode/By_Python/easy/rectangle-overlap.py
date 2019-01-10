# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-10 12:59:29
# @Last Modified time: 2019-01-10 13:08:05


class Solution:

    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        botton_left = (rec2[0], rec2[1])
        top_right = (rec2[2], rec2[3])
        botton_right = (rec2[2], rec2[1])
        top_left = (rec2[0], rec2[3])

        if botton_left[0] > rec1[0] and botton_left[0] < rec1[2] and botton_left[1] > rec1[1] and botton_left[1] < rec1[3]:
            return True
        if top_right[0] > rec1[0] and top_right[0] < rec1[2] and top_right[1] > rec1[1] and top_right[1] < rec1[3]:
            return True
        if botton_right[0] > rec1[0] and botton_right[0] < rec1[2] and botton_right[1] > rec1[1] and botton_right[1] < rec1[3]:
            return True
        if top_left[0] > rec1[0] and top_left[0] < rec1[2] and top_left[1] > rec1[1] and top_left[1] < rec1[3]:
            return True
        return False

if __name__ == '__main__':
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    solution = Solution()
    res = solution.isRectangleOverlap(rec1, rec2)
    print(res)
