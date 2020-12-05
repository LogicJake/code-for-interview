#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = defaultdict(int)

        for task in tasks:
            cnt[task] += 1

        max_task_num = max(cnt.values())

        res = (max_task_num - 1) * (n + 1)

        for _ in cnt.values():
            if _ == max_task_num:
                res += 1

        return max(res, len(tasks))


# @lc code=end
