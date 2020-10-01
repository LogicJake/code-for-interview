class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)

        status = [[0, 0, 0] for _ in range(n)]

        status[0][0] = int(leaves[0] == 'y')
        status[0][1] = status[0][2] = status[1][2] = 999999999

        for i in range(1, n):
            is_yellow = int(leaves[i] == 'y')
            is_red = int(leaves[i] == 'r')

            status[i][0] = status[i - 1][0] + is_yellow
            status[i][1] = min(status[i - 1][0], status[i - 1][1]) + is_red

            if i >= 2:
                status[i][2] = min(status[i - 1][1],
                                   status[i - 1][2]) + is_yellow

        return status[n - 1][2]
