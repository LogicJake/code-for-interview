nums = [6, 2, 5, 5, 3, 7, 3, 1, 1, 4, 4, 8, 8]
target = 10

n = len(nums)

if n == 0 or target == 0:
    print(0)

dp = [[0] * (target + 1) for _ in range(n)]
ans = 0

for i in range(0, n):
    dp[i][nums[i]] = 1

    if i != 0:
        for j in range(nums[i] + 1, target + 1):
            dp[i][j] = dp[i - 1][j - nums[i]]
    ans += dp[i][-1]

print(ans)
