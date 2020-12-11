#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        receive_bills = {5: 0, 10: 0}
        for num in bills:
            if num == 5:
                receive_bills[5] += 1
            elif num == 10:
                if receive_bills[5] == 0:
                    return False
                else:
                    receive_bills[5] -= 1
                    receive_bills[10] += 1
            elif num == 20:
                if receive_bills[5] > 0 and receive_bills[10] > 0:
                    receive_bills[5] -= 1
                    receive_bills[10] -= 1
                elif receive_bills[5] > 2:
                    receive_bills[5] -= 3
                else:
                    return False
        return True


# @lc code=end
