#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start


class LinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.head = LinkedNode()
        self.tail = LinkedNode()

        self.head.next = self.tail
        self.tail.pre = self.head

        self.capacity = capacity
        self.size = 0
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move2head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = LinkedNode(key, value)
            self.cache[key] = node
            self.add_head(node)

            self.size += 1

            if self.size > self.capacity:
                removed = self.remove_tail()
                self.cache.pop(removed.key)
                self.size -= 1

        else:
            node = self.cache[key]
            node.value = value
            self.move2head(node)

    def add_head(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def remove_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def move2head(self, node):
        self.remove_node(node)
        self.add_head(node)

    def remove_tail(self):
        node = self.tail.pre
        self.remove_node(node)

        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
