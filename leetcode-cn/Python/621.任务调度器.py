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

        cnt = list(cnt.values())
        next_times = [1] * len(cnt)

        time = 0
        for task in tasks:
            time += 1

            min_val_time = min(
                [next_times[i] for i in range(len(cnt)) if cnt[i] > 0])
            time = max(time, min_val_time)

            best = -1
            for i in range(len(cnt)):
                if cnt[i] > 0 and next_times[i] <= time:
                    if best == -1 or cnt[i] > cnt[best]:
                        best = i

            cnt[best] -= 1
            next_times[best] = time + n + 1

        return time


# @lc code=end
