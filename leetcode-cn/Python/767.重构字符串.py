#
# @lc app=leetcode.cn id=767 lang=python3
#
# [767] 重构字符串
#

# @lc code=start
from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2:
            return S

        length = len(S)
        counts = Counter(S)
        maxCount = max(counts.items(), key=lambda x: x[1])[1]
        if maxCount > (length + 1) // 2:
            return ""

        queue = [(-x[1], x[0]) for x in counts.items()]
        heapq.heapify(queue)
        ans = list()

        while len(queue) > 1:
            _, letter1 = heapq.heappop(queue)
            _, letter2 = heapq.heappop(queue)
            ans.extend([letter1, letter2])
            counts[letter1] -= 1
            counts[letter2] -= 1
            if counts[letter1] > 0:
                heapq.heappush(queue, (-counts[letter1], letter1))
            if counts[letter2] > 0:
                heapq.heappush(queue, (-counts[letter2], letter2))

        if queue:
            ans.append(queue[0][1])

        return "".join(ans)


# @lc code=end
