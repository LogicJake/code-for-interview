#
# @lc app=leetcode.cn id=341 lang=python3
#
# [341] 扁平化嵌套列表迭代器
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """


class NestedInteger:
    def isInteger(self) -> bool:
        """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """
        pass

    def getInteger(self) -> int:
        """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """
        pass

    def getList(self):
        """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """
        pass


class NestedIterator:
    def __init__(self, nestedList):
        self.data = []
        self.parse(nestedList)

    def parse(self, nestedList):
        for t in nestedList:
            if t.isInteger():
                self.data.append(t.getInteger())
            else:
                self.parse(t.getList())

    def next(self) -> int:
        return self.data.pop(0)

    def hasNext(self) -> bool:
        return len(self.data) != 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end
