# n = 3
# m = 7

# table = [[0, 3, 2], [3, 0, 3], [2, 1, 0]]

# pre = 1
# cur = 2

# for day in range(3, m + 1):
#     res = table[cur - 1][pre - 1]
#     pre = cur
#     cur = res

# print(cur)

line = input()
n, m = line.split(' ')
n = int(n)
m = int(m)

table = [[0] * n for _ in range(n)]

for i in range(n):
    line = input()
    nums = line.split(' ')

    for j in range(n):
        table[i][j] = int(nums[j])

pre = 1
cur = 2

for day in range(3, m + 1):
    res = table[cur - 1][pre - 1]
    pre = cur
    cur = res

print(cur)
