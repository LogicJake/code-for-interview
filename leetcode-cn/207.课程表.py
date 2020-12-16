#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        path = defaultdict(list)
        degree = defaultdict(int)

        for end, start in prerequisites:
            path[start].append(end)
            degree[end] += 1

        visited = 0
        queue = []
        for c in range(numCourses):
            if degree[c] == 0:
                queue.append(c)

        while queue:
            c = queue.pop(0)
            visited += 1
            for end in path[c]:
                degree[end] -= 1
                if degree[end] == 0:
                    queue.append(end)

        return visited == numCourses


# @lc code=end
