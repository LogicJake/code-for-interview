s = input()
n = 4
m = len(s)

cost = [0] * 5
cost[1] = min(100, 120)
cost[2] = min(200, 350)
cost[3] = min(360, 200)
cost[4] = min(220, 320)

dp = [[0] * m for _ in range(m)]

for i in range(1, m):
    for j in range(i - 1, -1, -1):
        dp[j][i] = min(dp[j + 1][i] + cost[int(s[j])],
                       dp[j][i - 1] + cost[int(s[i])])
        if s[i] == s[j]:
            dp[j][i] = min(dp[j][i], dp[j + 1][i - 1])

print(dp[0][m - 1])
