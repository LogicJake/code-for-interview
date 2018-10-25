# -*- coding: utf-8 -*-
# @Time    : 18-10-25 下午2:28
# @Author  : LogicJake
# @File    : uncommon_words_from_two_sentences.py


class Solution(object):
    """
        This problem is solved too complexly.
        the better solution:
        firstly, we count the number of occurrences of every word in both A and B,
        then words which appear once are what we want.
    """

    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        words_a = A.split(" ")
        words_a_plus = set([word for word in words_a if words_a.count(word) > 1])
        words_b = B.split(" ")
        words_b_plus = set([word for word in words_b if words_b.count(word) > 1])

        res = set()

        for word in set(words_a):
            if not word in words_b:
                res.add(word)

        for word in set(words_b):
            if not word in words_a:
                res.add(word)

        return list(res - words_a_plus - words_b_plus)


if __name__ == '__main__':
    solution = Solution()

    A = "s z z z s"
    B = "s z ejt"
    print(solution.uncommonFromSentences(A, B))
