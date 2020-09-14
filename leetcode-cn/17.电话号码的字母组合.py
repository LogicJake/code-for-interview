#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List

# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         digit_map = {
#             '2': 'abc',
#             '3': 'def',
#             '4': 'ghi',
#             '5': 'jkl',
#             '6': 'mno',
#             '7': 'pqrs',
#             '8': 'tuv',
#             '9': 'wxyz'
#         }

#         if len(digits) == 0:
#             return []

#         ans = list(digit_map[digits[0]])

#         def help(ans, nums):
#             new_ans = []
#             for a in ans:
#                 for n in nums:
#                     new_a = a + n
#                     new_ans.append(new_a)
#             return new_ans

#         for i in range(1, len(digits)):
#             ans = help(ans, list(digit_map[digits[i]]))


#         return ans
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits) == 0:
            return []

        def dfs(index):
            if index == len(digits):
                combinations.append(''.join(combination))
            else:
                for d in digit_map[digits[index]]:
                    combination.append(d)
                    dfs(index + 1)
                    combination.pop()

        combination = []
        combinations = []
        dfs(0)
        return combinations


# @lc code=end
