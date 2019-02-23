# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-02-23 12:30:05
# @Last Modified time: 2019-02-23 12:44:28


class Solution:

    def complexNumberMultiply(self, a: str, b: str) -> str:
        real_a, imaginary_a = a.split('+')
        real_b, imaginary_b = b.split('+')

        imaginary_a_num = imaginary_a.split('i')[0]
        imaginary_b_num = imaginary_b.split('i')[0]

        part_1 = int(real_a) * int(real_b)
        part_2 = int(real_a) * int(imaginary_b_num)
        part_3 = int(imaginary_a_num) * int(real_b)
        part_4 = -(int(imaginary_a_num) * int(imaginary_b_num))

        real_res = part_1 + part_4
        imaginary_res = part_2 + part_3

        return '{}+{}i'.format(real_res, imaginary_res)

if __name__ == '__main__':
    solution = Solution()
    a = "1+1i"
    b = "1+1i"
    res = solution.complexNumberMultiply(a, b)
    print(res)
