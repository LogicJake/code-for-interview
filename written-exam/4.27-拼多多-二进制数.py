x = input()
# x = '10001'
k = int(input())
x = int(x, 2)


def count_one(n):
    cnt = 0
    while n > 0:
        if n != 0:
            n = n & (n - 1)
        cnt += 1
    return cnt


res = x
while (True):
    x = x + 1
    if count_one(x) == k:
        res = x
        break

res = bin(res).replace('0b', '')
print(res)
