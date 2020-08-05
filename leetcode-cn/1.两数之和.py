#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, value1 in enumerate(nums):
            # 这里每一次迭代都要重置，否则 result 会保存上一轮的无用结果
            result = []

            # 可以出现 = ，即有一个整数为0
            '''
            if value1 <= target:
                result.append(i)
                target2 = target - value1

                for j, value2 in enumerate(nums):
                    if j == i:
                        continue
                    if value2 == target2:
                        result.append(j)
                        return result
            '''
            result.append(i)
            target2 = target - value1

            for j, value2 in enumerate(nums):
                if j == i:
                    continue
                if value2 == target2:
                    result.append(j)
                    return result


# @lc code=end
