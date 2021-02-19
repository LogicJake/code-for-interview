from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = 0

        for num in nums:
            ret = ret ^ num

        div = 1
        while div & ret == 0:
            div <<= 1

        a = 0
        b = 0

        for num in nums:
            if num & div:
                a = a ^ num
            else:
                b = b ^ num

        return [a, b]
