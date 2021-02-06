from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        x = None
        for num in nums:
            if votes == 0:
                x = num

            if num == x:
                votes += 1
            else:
                votes -= 1
        return x
