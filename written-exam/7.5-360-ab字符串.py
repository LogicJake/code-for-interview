s = input()

ans = 0
cnt = 0

for c in s[::-1]:
    if c == 'b':
        cnt += 1
    else:
        ans = ans + cnt
        cnt *= 2

print(ans % 1000000007)