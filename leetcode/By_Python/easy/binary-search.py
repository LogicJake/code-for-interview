# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-02-13 20:45:01
# @Last Modified time: 2019-02-13 20:59:10


class Solution:

    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        i = 0
        j = len(nums) - 1
        while(i <= j):
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                return mid
        return -1

if __name__ == '__main__':
    nums = [5]
    target = 5
    solution = Solution()
    res = solution.search(nums, target)
    print(res)
