#
# @lc app=leetcode.cn id=381 lang=python3
#
# [381] O(1) 时间插入、删除和获取随机元素 - 允许重复
#

# @lc code=start
from random import choice
from collections import defaultdict


class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.idx = defaultdict(set)
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val not in self.idx:
            self.idx[val].add(len(self.nums))
            self.nums.append(val)
            return True
        else:
            self.idx[val].add(len(self.nums))
            self.nums.append(val)
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if len(self.idx[val]) != 0:
            remove_id = self.idx[val].pop()
            last_num = self.nums[-1]

            self.idx[last_num].add(remove_id)
            self.idx[last_num].discard(len(self.nums) - 1)

            self.nums[remove_id] = last_num
            self.nums.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
