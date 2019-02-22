# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-02-19 16:27:45
# @Last Modified time: 2019-02-22 14:54:38
from math import ceil


class Solution:

    def spiralMatrixIII(self, R: 'int', C: 'int', r0: 'int', c0: 'int') -> 'List[List[int]]':
        rc = [0, 1, 0, -1]
        cc = [1, 0, -1, 0]
        cur_direction = 0
        res = [[r0, c0]]
        cur_r = r0
        cur_c = c0
        visited = []
        visited.append(r0 * C + c0)
        while len(res) != R * C:
            next_r = cur_r + rc[cur_direction]
            next_c = cur_c + cc[cur_direction]

            pos = next_r * C + next_c
            if 0 <= next_r < R and 0 <= next_c < C and pos not in visited:
                visited.append(pos)
                cur_r = next_r
                cur_c = next_c
                cur_direction = (cur_direction + 1) % 4
                res.append([next_r, next_c])
            elif next_r < 0 or next_r >= R or next_c < 0 or next_c >= C:
                cur_r = next_r
                cur_c = next_c
                cur_direction = (cur_direction + 1) % 4
            elif pos in visited:
                cur_direction = (cur_direction - 1) % 4

        return res


class Solution2:

    def spiralMatrixIII(self, R: 'int', C: 'int', r0: 'int', c0: 'int') -> 'List[List[int]]':
        rc = [0, 1, 0, -1]
        cc = [1, 0, -1, 0]
        cur_direction = 0
        res = [[r0, c0]]
        cur_r = r0
        cur_c = c0
        k = 1
        while len(res) != R * C:
            dk = ceil(k / 2)
            for i in range(1, dk + 1):
                next_r = cur_r + rc[cur_direction]
                next_c = cur_c + cc[cur_direction]
                if 0 <= next_r < R and 0 <= next_c < C:
                    res.append([next_r, next_c])
                cur_r = next_r
                cur_c = next_c
            cur_direction = (cur_direction + 1) % 4
            k += 1

        return res


if __name__ == '__main__':
    solution = Solution2()
    R = 5
    C = 6
    r0 = 1
    c0 = 4
    solution.spiralMatrixIII(R, C, r0, c0)
