from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums_a = []
        cnt = 0

        for num in nums:
            if num == 0:
                cnt += 1
            else:
                nums_a.append(num)

        nums_a.sort()

        for i in range(len(nums_a)):
            if i != 0:
                diff = nums_a[i] - nums_a[i - 1] - 1
                if diff < 0:
                    return False
                cnt -= diff
                if cnt < 0:
                    return False

        return True
