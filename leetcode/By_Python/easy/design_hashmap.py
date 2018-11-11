# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-11-11 14:30:17
# @Last Modified time: 2018-11-11 15:34:09


class my_pair:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value


class MyHashMap:

    def hash(self, key):
        return key % self.capacity

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 10
        self.factory = [None] * self.capacity

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = self.hash(key)
        node = my_pair(key, value)
        if self.factory[index] is None:
            self.factory[index] = node
        elif isinstance(self.factory[index], my_pair):
            if self.factory[index].get_key() == key:
                self.factory[index].set_value(value)
            else:
                first_pair = self.factory[index]
                second_pair = node
                self.factory[index] = [first_pair, second_pair]
        elif isinstance(self.factory[index], list):
            loc = -1
            pairs = self.factory[index]
            for i, pair in enumerate(pairs):
                if pair.get_key() == key:
                    loc = i
                    break

            if loc == -1:
                self.factory[index].append(node)
                self.size_increase()
            else:
                self.factory[index][loc].set_value(value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = self.hash(key)
        if self.factory[index] is None:
            return -1
        elif isinstance(self.factory[index], my_pair):
            if self.factory[index].get_key() == key:
                return self.factory[index].get_value()
            else:
                return -1
        elif isinstance(self.factory[index], list):
            pairs = self.factory[index]
            for pair in pairs:
                if pair.get_key() == key:
                    return pair.get_value()
            return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = self.hash(key)
        if isinstance(self.factory[index], my_pair):
            if self.factory[index].get_key() == key:
                self.factory[index] = None
        elif isinstance(self.factory[index], list):
            loc = -1
            pairs = self.factory[index]
            for i, pair in enumerate(pairs):
                if pair.get_key() == key:
                    loc = i
                    break
            if loc != -1:
                del self.factory[index][loc]

if __name__ == '__main__':
    obj = MyHashMap()
    obj.put(1, 1)
    print(obj.get(1))
    obj.put(1, 3)
    print(obj.get(1))
    obj.put(11, 2)
    print(obj.get(11))
    obj.put(11, 5)
    print(obj.get(11))
    obj.remove(11)
    print(obj.get(11))
