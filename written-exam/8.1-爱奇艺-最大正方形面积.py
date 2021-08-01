raw_input = input("")

m = raw_input.split(';')

matrix = []

for line in m:

    elements = line.split(',')

    matrix.append(elements)

if len(matrix) == 0 or len(matrix[0]) == 0:
    print(0)

ans = 0
m = len(matrix)
n = len(matrix[0])

dp = [[0] * n for _ in range(m)]

for i in range(m):
    if matrix[i][0] == '1':
        dp[i][0] = 1
    ans = max(ans, dp[i][0])

for i in range(n):
    if matrix[0][i] == '1':
        dp[0][i] = 1
    ans = max(ans, dp[0][i])

for i in range(m):
    for j in range(n):
        if matrix[i][j] == '1':
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                               dp[i - 1][j - 1]) + 1

            ans = max(ans, dp[i][j])

print(ans * ans)
