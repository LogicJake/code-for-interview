#
# @lc app=leetcode.cn id=1203 lang=python3
#
# [1203] 项目管理
#

# @lc code=start
from typing import List
import collections


class Solution:
    def topological_sort(self, items, indegree, neighbors):
        # 建立队列和访问顺序
        queue = collections.deque()
        res = []

        # 初始化队列
        for item in items:
            if not indegree[item]:
                queue.append(item)

        if not queue:
            return []

        # BFS
        while queue:
            cur = queue.popleft()
            res.append(cur)

            # 遍历邻居节点
            for neighbor in neighbors[cur]:
                indegree[neighbor] -= 1
                if not indegree[neighbor]:
                    queue.append(neighbor)

        return res

    def sortItems(self, n: int, m: int, group: List[int],
                  beforeItems: List[List[int]]) -> List[int]:
        max_group_id = m
        for task in range(n):
            if group[task] == -1:
                group[task] = max_group_id
                max_group_id += 1

        task_indegree = [0] * n
        group_indegree = [0] * max_group_id
        task_neighbors = [[] for _ in range(n)]
        group_neighbors = [[] for _ in range(max_group_id)]
        group_to_tasks = [[] for _ in range(max_group_id)]

        for task in range(n):
            group_to_tasks[group[task]].append(task)

            for prerequisite in beforeItems[task]:

                # 判断相关联的两个项目是否属于同一组
                if group[prerequisite] != group[task]:

                    # 不是同组，给小组建图
                    group_indegree[group[task]] += 1
                    group_neighbors[group[prerequisite]].append(group[task])
                else:
                    # 同组，给组内项目建图
                    task_indegree[task] += 1
                    task_neighbors[prerequisite].append(task)

        res = []

        # 得到小组的访问顺序
        group_queue = self.topological_sort([i for i in range(max_group_id)],
                                            group_indegree, group_neighbors)

        if len(group_queue) != max_group_id:
            return []

        for group_id in group_queue:
            # 得到每组项目的访问顺序
            task_queue = self.topological_sort(group_to_tasks[group_id],
                                               task_indegree, task_neighbors)

            if len(task_queue) != len(group_to_tasks[group_id]):
                return []
            res += task_queue

        return res


# @lc code=end
