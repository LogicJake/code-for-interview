#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] 常数时间插入、删除和获取随机元素
#

# @lc code=start
from random import choice


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            last_num = self.nums[-1]
            index = self.dict[val]

            self.nums[index] = last_num
            self.dict[last_num] = index
            del self.dict[val]
            self.nums.pop()
            return True

        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
