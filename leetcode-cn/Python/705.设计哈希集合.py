#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#


# @lc code=start
class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def add(self, key: int) -> None:
        pos = self.hash(key)
        if key not in self.table[pos]:
            self.table[pos].append(key)

    def remove(self, key: int) -> None:
        pos = self.hash(key)
        if key in self.table[pos]:
            self.table[pos].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        pos = self.hash(key)
        return key in self.table[pos]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end
