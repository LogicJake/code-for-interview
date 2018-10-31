# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-10-31 19:00:11
# @Last Modified time: 2018-10-31 19:16:27


class Solution(object):

    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split(' ')

        t_words = []
        print(words)
        for index, word in enumerate(words):
            if word[0].lower() == 'a' or word[0].lower() == 'e' or word[0].lower() == 'i' or word[0].lower() == 'o' or word[0].lower() == 'u':
                new_word = word + 'ma'
            else:
                new_word = word[1:] + word[0] + 'ma'

            new_word += (index + 1) * 'a'
            t_words.append(new_word)
        return ' '.join(t_words)


if __name__ == '__main__':
    solution = Solution()

    sentence = "Each word consists of lowercase and uppercase letters only"
    res = solution.toGoatLatin(sentence)
    print(res)
