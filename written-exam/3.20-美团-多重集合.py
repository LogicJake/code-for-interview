# n = 6
# m = 8

# table = [[1, 1, 4, 5, 1, 4], [3, 0, 4, 0, 3, 0]]

# num1 = list(set(table[0]))
# num1.sort()
# num2 = list(set(table[1]))
# num2.sort()

# print(num1, num2)
# diff = num1[0] - num2[0]

# print(m - diff % m)

line = input()
n, m = line.split(' ')
n = int(n)
m = int(m)

table = [[0] * n, [0] * n]
for i in range(2):
    line = input()
    nums = line.split(' ')

    for j in range(n):
        table[i][j] = int(nums[j])

num1 = list(set(table[0]))
num1.sort()
num2 = list(set(table[1]))
num2.sort()

ans_list = []

for i in range(len(num2)):
    diff = num1[0] - num2[0]
    ans_list.append(m - diff % m)


def check(ans, nums):
    for num in nums:
        if (ans - num) % m != 0:
            return False

    return True


for i in range(99):
    ans = ans_list[0] + i * m
    if check(ans, ans_list[1:]):
        break

print(ans)
