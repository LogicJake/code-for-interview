'''
@Author: LogicJake
@Date: 2019-05-23 09:52:09
@LastEditTime: 2019-05-23 10:15:20
'''


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        search_dict = dict()
        words = str.split(' ')

        # 不判断相等则可能出现index out of range
        if len(words) != len(pattern):
            return False

        for index, p in enumerate(pattern):
            if p in search_dict:
                if search_dict[p] != words[index]:
                    return False
            else:
                # 不同pattern对应的word应该也不相等
                if words[index] in search_dict.values():
                    return False
                search_dict[p] = words[index]

        return True


if __name__ == "__main__":
    pattern = "abba"
    str = "dog dog dog dog"

    solution = Solution()
    res = solution.wordPattern(pattern, str)
