N = input()
N = int(N)

lines = []

for _ in range(N):
    li = input()
    l, r = li.split(' ')
    l = int(l)
    r = int(r)

    lines.append([l, r])

# lines = [[2, 3], [1, 9], [4, 10], [5, 20]]

lines.sort()
ans = 'false'
for i in range(1, len(lines)):
    if lines[i][1] <= lines[i-1][1]:
        ans = 'true'

print(ans)
