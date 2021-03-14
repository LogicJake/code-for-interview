#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#


# @lc code=start
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1009
        self.table = [{} for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        pos = self.hash(key)
        self.table[pos][key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        pos = self.hash(key)

        if key in self.table[pos]:
            return self.table[pos][key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        pos = self.hash(key)

        if key in self.table[pos]:
            del self.table[pos][key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end
