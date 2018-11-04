# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-11-04 12:36:05
# @Last Modified time: 2018-11-04 12:36:14


class RecentCounter(object):

    def __init__(self):
        self.q = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)
        while self.q[0] < t - 3000:
            del self.q[0]
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
