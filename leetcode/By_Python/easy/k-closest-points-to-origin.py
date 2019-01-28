# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-26 17:57:28
# @Last Modified time: 2019-01-26 18:13:52

import functools


class Solution:

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key=lambda point: point[0]**2 + point[1]**2)
        return points[:K]

if __name__ == '__main__':
    solution = Solution()
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    solution.kClosest(points, K)
