# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-28 14:14:47
# @Last Modified time: 2019-01-28 14:36:50


class Solution:

    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order = order.rjust(len(order) + 1, ',')
        for i in range(len(words) - 1):
            first_word = words[i]
            second_word = words[i + 1]

            length = max(len(first_word), len(second_word))

            first_word = first_word.ljust(length, ',')
            second_word = second_word.ljust(length, ',')

            for j in range(length):
                first_word_char = first_word[j]
                second_word_char = second_word[j]

                first_word_char_index = order.find(first_word_char)
                second_word_char_index = order.find(second_word_char)
                if first_word_char_index < second_word_char_index:
                    break
                elif first_word_char_index > second_word_char_index:
                    return False

        return True

if __name__ == '__main__':
    words = ["fxasxpc", "dfbdrifhp", "nwzgs", "cmwqriv", "ebulyfyve",
             "miracx", "sxckdwzv", "dtijzluhts", "wwbmnge", "qmjwymmyox"]
    order = "zkgwaverfimqxbnctdplsjyohu"

    solution = Solution()
    res = solution.isAlienSorted(words, order)
    print(res)
