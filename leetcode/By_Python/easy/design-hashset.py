# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-12-08 15:17:36
# @Last Modified time: 2018-12-08 15:50:07


class MyHashSet:

    def my_hash(self, data):
        return data % 100

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = [[]] * 100

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        index = self.my_hash(key)
        if not self.contains(key):
            self.storage[index].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        index = self.my_hash(key)
        if self.contains(key):
            self.storage[index].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        index = self.my_hash(key)
        for i in self.storage[index]:
            if i == key:
                return True
        return False

if __name__ == '__main__':
    hashSet = MyHashSet()
    hashSet.contains(1)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
