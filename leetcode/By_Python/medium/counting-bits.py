# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-02-19 15:23:35
# @Last Modified time: 2019-02-19 16:20:02


class Solution:

    def countBits(self, num: 'int') -> 'List[int]':
        res = []
        pre = 0
        for i in range(num + 1):
            if i == 0:
                res.append(0)
            elif i % 4 == 0:
                if i & (i - 1) == 0:
                    res.append(1)
                    pre = i
                else:
                    res.append(res[pre] + res[i - pre])
            elif i % 2 == 1:
                res.append(res[-1] + 1)
            else:
                res.append(res[-1])

        return res

if __name__ == '__main__':
    solution = Solution()
    num = 64
    res = solution.countBits(num)
    print(res)
