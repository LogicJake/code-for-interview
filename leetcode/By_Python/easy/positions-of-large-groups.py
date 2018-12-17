# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-12-08 14:49:53
# @Last Modified time: 2018-12-08 15:05:13


class Solution:

    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        start = 0
        pre_c = S[0]
        res = []
        for i in range(1, len(S)):
            if S[i] != pre_c:
                pre_c = S[i]
                if i - start >= 3:
                    tmp = [start, i - 1]
                    res.append(tmp)
                start = i
        if len(S) - start >= 3:
            tmp = [start, len(S) - 1]
            res.append(tmp)
        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    S = "aaa"
    solution.largeGroupPositions(S)
