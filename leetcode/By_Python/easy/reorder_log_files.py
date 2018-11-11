# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-11-11 12:33:36
# @Last Modified time: 2018-11-11 13:40:50


class Solution:

    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digits = []
        letters = []
        for log in logs:
            if log.split(' ')[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: x.split(" ")[0], reverse=True)
        letters.sort(key=lambda x: x.split(" ")[1])
        return letters + digits

if __name__ == '__main__':
    solution = Solution()
    logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7",
            "ab1 off key dog", "a8 act zoo"]
    res = solution.reorderLogFiles(logs)
    print(res)
