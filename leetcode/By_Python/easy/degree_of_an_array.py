# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-11-16 12:44:17
# @Last Modified time: 2018-11-16 13:24:46

from collections import Counter


class Solution:

    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reverse_nums = nums[:]
        reverse_nums.reverse()

        num_counts = Counter(nums)
        most_commons = num_counts.most_common()

        max_num = most_commons[0][1]
        res = 99999999
        for most_common in most_commons:
            if most_common[1] == max_num:
                value = most_common[0]
                start_index = nums.index(value)
                end_index = reverse_nums.index(value)
                res = min(res, len(nums) - end_index - start_index)
            else:
                break
        return res

if __name__ == '__main__':
    solution = Solution()

    nums = [1, 2, 2, 3, 1]
    res = solution.findShortestSubArray(nums)
    print(res)
