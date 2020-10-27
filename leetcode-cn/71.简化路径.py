#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#


# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')

        stack = []
        for p in path:
            if p == '' or p == '.':
                continue

            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)

        return '/' + '/'.join(stack)


# @lc code=end
