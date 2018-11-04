# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-11-04 13:36:39
# @Last Modified time: 2018-11-04 14:04:46


class Solution:

    def count(self, word):
        chars = dict()
        for c in word:
            if c.isalpha():
                num = chars.get(c.lower(), 0)
                chars[c.lower()] = num + 1

        return chars

    def cmp(self, dict1, dict2):
        for key in dict1.keys():
            if dict1[key] > dict2.get(key, -1):
                return False
        return True

    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        res = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

        chars = self.count(licensePlate)
        print(chars)
        for word in words:
            tmp = self.count(word)
            print(tmp)
            if self.cmp(chars, tmp):
                if len(word) < len(res):
                    res = word

        return res

if __name__ == '__main__':
    solution = Solution()
    licensePlate = "1s3 PSt"
    words = ["looks", "pest", "stew", "show"]
    res = solution.shortestCompletingWord(licensePlate, words)
    print(res)
