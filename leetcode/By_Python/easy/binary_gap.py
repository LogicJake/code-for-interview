# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-10-29 14:19:25
# @Last Modified time: 2018-10-29 14:35:50


class Solution(object):

    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        pre = 100
        max_value = 0
        i = 0
        while N != 0:
            a = N % 2
            N /= 2
            if a == 1:
                if i - pre > max_value:
                    max_value = i - pre
                pre = i
            i += 1

        return max_value

if __name__ == '__main__':
    solution = Solution()

    res = solution.binaryGap(6)
    print(res)
