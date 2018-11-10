# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-11-10 14:04:30
# @Last Modified time: 2018-11-10 14:20:29


class Solution:

    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five_num = 0
        ten_num = 0
        for m in bills:
            if m == 5:
                five_num += 1
            elif m == 10:
                ten_num += 1
            print(five_num, ten_num)
            change = m - 5
            if change == 5:
                five_num -= 1
                if five_num < 0:
                    return False
            if change == 15:
                if ten_num > 0:
                    ten_num -= 1
                    five_num -= 1
                    if five_num < 0:
                        return False

                else:
                    five_num -= 3
                    if five_num < 0:
                        return False
        return True

if __name__ == '__main__':
    solution = Solution()
    bills = [5, 5, 5, 5, 10, 5, 10, 10, 10, 20]
    print(solution.lemonadeChange(bills))
