#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
from typing import List
'''
class Solution:
    def threeSum(self, nums, target):
        result = []
        length = len(nums)

        for first in range(length):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            new_target = target - nums[first]

            third = length - 1
            for second in range(first + 1, length):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[
                        third] > new_target:
                    third -= 1

                if second == third:
                    break

                if nums[second] + nums[third] == new_target:
                    result.append([nums[first], nums[second], nums[third]])

        return result

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        nums.sort()
        # 保证有三个数
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            result_part = self.threeSum(nums[i + 1:], target - nums[i])

            for r in result_part:
                result.append([nums[i]] + r)

        return result
'''


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        nums.sort()

        def help(start, target):
            if target == 0 and len(path) == 4:
                ans.append(path[:])
                return

            for i in range(start, n):
                '''
                这一步为什么不能是nums[i] == nums[i + 1]（1）
                如果出现连续的两个值都要入path，那么按照（1）所描述，会直接进入第一次dfs选择第二个值；
                然后下一次dfs就不能选择前一个值。
                '''
                if i - 1 >= start and nums[i] == nums[i - 1]:
                    continue

                # 剪枝
                if i + 1 < n and nums[i] + nums[i + 1] * (3 -
                                                          len(path)) > target:
                    break

                if i + 1 < n and nums[i] + nums[n - 1] * (3 -
                                                          len(path)) < target:
                    continue

                path.append(nums[i])
                help(i + 1, target - nums[i])
                path.pop()

        help(0, target)

        return ans


# @lc code=end
