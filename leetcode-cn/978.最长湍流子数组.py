from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)

        left = 0
        right = 0
        ans = 1

        while right < n - 1:
            if left == right:
                if arr[left] == arr[left + 1]:
                    left += 1
                right += 1
            else:
                if arr[right - 1] < arr[right] and arr[right] > arr[right + 1]:
                    right += 1
                elif arr[right - 1] > arr[right] and arr[right] < arr[right +
                                                                      1]:
                    right += 1
                else:
                    left = right

            ans = max(ans, right - left + 1)

        return ans
