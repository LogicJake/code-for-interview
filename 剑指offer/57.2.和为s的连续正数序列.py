from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        right = 1
        left = 1
        sum_ = 0
        ans = []
        while left < target // 2:
            if sum_ > target:
                sum_ -= left
                left += 1
            elif sum_ < target:
                sum_ += right
                right += 1
            else:
                ans.append(list(range(left, right)))
                sum_ -= left
                left += 1
        return ans
