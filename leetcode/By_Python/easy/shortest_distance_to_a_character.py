# -*- coding: utf-8 -*-
# @Time    : 18-10-24 下午1:23
# @Author  : LogicJake
# @File    : shortest_distance_to_a_character.py


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        index_of_c = []
        res = []
        for i in range(len(S)):
            if S[i] == C:
                index_of_c.append(i)

        for i in range(len(S)):
            distances = [abs(index - i) for index in index_of_c]
            res.append(min(distances))
        return res


if __name__ == '__main__':
    S = "loveleetcode"
    C = 'e'
    solution = Solution()
    res = solution.shortestToChar(S, C)
    print(res)
