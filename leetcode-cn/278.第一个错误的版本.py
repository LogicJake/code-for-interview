#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2

            if not isBadVersion(mid):
                left = mid + 1
            if isBadVersion(mid):
                if mid - 1 < 0 or not isBadVersion(mid - 1):
                    return mid
                else:
                    right = mid - 1


# @lc code=end
