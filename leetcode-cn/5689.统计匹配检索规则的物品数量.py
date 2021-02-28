from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str,
                     ruleValue: str) -> int:
        if ruleKey == 'type':
            index = 0
        if ruleKey == 'color':
            index = 1
        if ruleKey == 'name':
            index = 2

        ans = 0

        for item in items:
            if item[index] == ruleValue:
                ans += 1

        return ans
