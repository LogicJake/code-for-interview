class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.mem = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add2head(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node

    def move2head(self, node):
        self.remove(node)
        self.add2head(node)

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def remove_tail(self):
        node = self.tail.prev
        self.remove(node)
        return node.key

    def set(self, key, value):
        if key not in self.mem:
            node = Node(key, value)
            self.mem[key] = node
            self.size += 1
            self.add2head(node)

            if self.size > self.capacity:
                key = self.remove_tail()
                del self.mem[key]
                self.size -= 1
        else:
            node = self.mem[key]
            node.value = value
            self.move2head(node)

    def get(self, key):
        if key not in self.mem:
            return -1
        else:
            node = self.mem[key]
            self.move2head(node)
            return node.value


class Solution:
    def LRU(self, operators, k):
        ans = []
        cache = LRUCache(k)

        for operator in operators:
            opt = operator[0]

            if opt == 1:
                key = operator[1]
                value = operator[2]
                cache.set(key, value)
            else:
                key = operator[1]
                value = cache.get(key)
                ans.append(value)

        return ans
