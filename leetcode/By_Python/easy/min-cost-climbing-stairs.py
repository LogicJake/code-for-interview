# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-10 12:48:26
# @Last Modified time: 2019-01-10 12:55:45


class Solution:

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        min_cost = [0 for i in range(len(cost))]
        for i in range(len(cost)):
            if i <= 1:
                min_cost[i] = cost[i]
            else:
                min_cost[i] = cost[i] + min(min_cost[i - 1], min_cost[i - 2])
        return min(min_cost[len(cost) - 2], min_cost[len(cost) - 1])
if __name__ == '__main__':
    solution = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    res = solution.minCostClimbingStairs(cost)
    print(res)
