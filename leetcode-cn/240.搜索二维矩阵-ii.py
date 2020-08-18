#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#


# @lc code=start
class Solution:
    def helper(self, matrix, start, target, flag):
        l = start
        # 横向
        if flag:
            r = len(matrix[0]) - 1
        else:
            r = len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2

            if flag:
                if matrix[start][mid] < target:
                    l = mid + 1
                elif matrix[start][mid] > target:
                    r = mid - 1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    l = mid + 1
                elif matrix[mid][start] > target:
                    r = mid - 1
                else:
                    return True

        return False

    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False

        for i in range(min(len(matrix), len(matrix[0]))):
            left = self.helper(matrix, i, target, True)
            right = self.helper(matrix, i, target, False)

            if left or right:
                return True
        return False

    # def searchMatrix(self, matrix, target):
    #     """
    #     :type matrix: List[List[int]]
    #     :type target: int
    #     :rtype: bool
    #     """
    #     if len(matrix) == 0:
    #         return False

    #     row = 0
    #     col = len(matrix[0]) - 1

    #     while row >= 0 and row < len(matrix) and col >= 0 and col < len(
    #             matrix[0]):

    #         if target > matrix[row][col]:
    #             row += 1
    #         elif target < matrix[row][col]:
    #             col -= 1
    #         else:
    #             return True
    #     return False


# @lc code=end
