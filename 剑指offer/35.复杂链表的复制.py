# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        mem = {}

        cur = head
        while cur:
            mem[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            mem[cur].next = mem.get(cur.next)
            mem[cur].random = mem.get(cur.random)
            cur = cur.next

        return mem[head]