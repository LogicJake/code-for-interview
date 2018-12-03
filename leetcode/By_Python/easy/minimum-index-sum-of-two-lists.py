# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-12-03 12:45:40
# @Last Modified time: 2018-12-03 12:56:09


class Solution:

    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        intersectionList = list(set(list1).intersection(set(list2)))
        min_sum = 9999999999999
        for a in intersectionList:
            index1 = list1.index(a)
            index2 = list2.index(a)
            if index1 + index2 < min_sum:
                min_sum = index1 + index2
                res = [a]
            elif index1 + index2 == min_sum:
                res.append(a)
        return res


if __name__ == '__main__':
    solution = Solution()

    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Burger King", "Tapioca Express", "Shogun"]
    res = solution.findRestaurant(list1, list2)
    print(res)
