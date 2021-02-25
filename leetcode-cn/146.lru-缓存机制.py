#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start


class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def addHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def moveHead(self, node):
        # 断开在原链表中的连接
        self.removeNode(node)
        self.addHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node.key

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # 移到队首
            self.moveHead(node)
            res = node.value
            return res
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            # 移到队首
            self.moveHead(node)
        else:
            node = Node()
            node.key = key
            node.value = value
            self.cache[key] = node
            # 添加到队首
            self.addHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 移除队尾
                key = self.removeTail()
                del self.cache[key]
                self.size -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
