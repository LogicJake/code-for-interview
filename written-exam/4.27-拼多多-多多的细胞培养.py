# 3 = 1 + 2 = 2**0 + 2**1
# 5 = 1 + 4 = 2**0 + 2**2
# 2 = 2**1

import math


def help(N):
    M = 0
    ans = []

    while N > 0:
        res = math.log2(N)
        res = int(res)
        M = max(res, M)
        ans.append(res)
        N = N - 2**res

    M = M + 1
    ans = [str(M - a) for a in ans]

    return M, ans


T = int(input())
for _ in range(T):
    N = int(input())
    M, ans = help(N)
    print(M)
    print(' '.join(ans))
