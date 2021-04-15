n = int(input())
nums = []
line = input()
line = line.split(' ')
for i in range(n):
    nums.append(int(line[i]))

if n == 0:
    print(0)

dp = [float('inf')] * n
dp[0] = 0

for i in range(n):
    dis = nums[i]

    for j in range(i, min(i + dis + 1, n)):
        dp[j] = min(dp[j], dp[i] + 1)

print(dp[-1])