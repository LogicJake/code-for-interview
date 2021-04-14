#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#

# @lc code=start
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_visted = [False] * len(rooms)
        keys_stack = []

        # 初始化栈
        for key in rooms[0]:
            keys_stack.append(key)
        rooms_visted[0] = True

        while len(keys_stack) != 0:
            new_room = keys_stack.pop()
            if rooms_visted[new_room]:
                continue

            rooms_visted[new_room] = True
            for key in rooms[new_room]:
                keys_stack.append(key)

        return sum(rooms_visted) == len(rooms)


# @lc code=end
