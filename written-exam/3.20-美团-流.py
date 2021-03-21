source = 'abcdefghijklmnopqrstuvwxyz'
target = 'z'

mem = {}
total = len(source)
ans = 0

for index, c in enumerate(source):
    mem[c] = index

cnt = 1
for index in range(1, len(target)):
    if mem[target[index]] > mem[target[index - 1]]:
        cnt += 1
    else:
        ans += total - cnt
        cnt = 1

ans += (mem[target[-1]] - cnt + 1)

print(ans)
