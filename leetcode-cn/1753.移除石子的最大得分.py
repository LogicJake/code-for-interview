import heapq


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        ans = 0

        arr = [-a, -b, -c]
        heapq.heapify(arr)

        while True:
            max_num = -heapq.heappop(arr)
            median_num = -heapq.heappop(arr)
            min_num = arr[0]

            print(max_num, median_num)

            if median_num == 0:
                break

            cnt = max(median_num - min_num, 1)
            ans += cnt

            median_num -= cnt
            max_num -= cnt

            heapq.heappush(arr, -max_num)
            heapq.heappush(arr, -median_num)

        return ans
