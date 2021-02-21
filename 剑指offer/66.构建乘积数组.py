from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        pre = []
        after = []

        pre_value = 1
        for i in range(len(a)):
            if i == 0:
                pre.append(1)
            else:
                pre_value = pre_value * a[i - 1]
                pre.append(pre_value)

        after_value = 1
        for i in range(len(a)):
            if i == 0:
                after.append(1)
            else:
                after_value = after_value * a[len(a) - i]
                after.append(after_value)
        after = after[::-1]

        ans = []
        for i in range(len(a)):
            ans.append(after[i] * pre[i])
        return ans
