n = 4
a = [2, 0, 2, 0]

un = len(set(a))
cnt = [0] * 10
for num in a:
    cnt[num] += 1

ans = 0
path = []
first = True


def dfs(cnt):
    global ans, first
    if len(set(path)) == un:
        ans += 1

    for i in range(10):
        if i == 0 and first:
            first = False
            continue

        if cnt[i] != 0:
            path.append(i)
            cnt[i] -= 1
            dfs(cnt)
            path.pop(-1)
            cnt[i] += 1


dfs(cnt)
print(ans)
