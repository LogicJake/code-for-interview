# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-09 12:34:47
# @Last Modified time: 2019-01-09 12:54:26


class Solution:

    # first version
    def maximumProduct_(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negative_nums = []
        for i in nums:
            if i < 0:
                negative_nums.append(i)
        if len(negative_nums) <= 1 or len(negative_nums) == len(nums):
            nums.sort()
            return nums[-3] * nums[-2] * nums[-1]
        else:
            nums.sort()
            negative_nums.sort()
            negative_product = negative_nums[0] * negative_nums[1] * nums[-1]
            postive_product = nums[-3] * nums[-2] * nums[-1]
            return max(negative_product, postive_product)

    # second version(better)
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])

if __name__ == '__main__':
    solution = Solution()
    nums = [-4, -3, 2, 34, 15, 60]
    res = solution.maximumProduct(nums)
    print(res)
