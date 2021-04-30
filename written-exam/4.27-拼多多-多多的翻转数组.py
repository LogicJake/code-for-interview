n = int(input())
line = input().split(' ')
arr = [int(a) for a in line]

# n = 5
# arr = [1, 0, 0, 1, 0]

mirror_arr = [0] * n
for i in range(n):
    mirror_arr[i] = 1 if arr[i] == 0 else -1

start, end = 0, 0

pre = mirror_arr[0]
max_ = pre
start, end = 0, 0
max_start, max_end = 0, 0
for i in range(1, n):
    if pre + mirror_arr[i] > mirror_arr[i]:
        end = i
        pre = pre + mirror_arr[i]
    else:
        start = end = i
        pre = mirror_arr[i]

    if pre > max_:
        max_ = pre
        max_start = start
        max_end = end

res = 0
for i in range(n):
    if arr[i] == 1 and (i < max_start or i > max_end):
        res += 1
    elif arr[i] == 0 and (i >= max_start and i <= max_end):
        res += 1
print(res)
