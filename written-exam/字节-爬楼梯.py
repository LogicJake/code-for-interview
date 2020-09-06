def function(N):
    if N < 2:
        return N

    dp = [[0] * 2 for i in range(N + 1)]
    dp[0] = [1, 0]
    dp[1] = [1, 0]

    for i in range(2, N + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        dp[i][1] = dp[i - 2][0]

    return dp[N][0] + dp[N][1]


print(function(6))
