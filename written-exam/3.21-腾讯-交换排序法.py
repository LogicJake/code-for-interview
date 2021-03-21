a = [5, 4, 2, 3, 1]
pos = [4]

n = len(a)
res = 'YES'
for i in range(n - 1):
    flag = True
    for j in range(n - i - 1):
        if a[i] < a[i + 1]:
            if i + 1 in pos:
                res = 'NO'
                break
            else:
                a[i + 1], a[i] = a[i], a[i + 1]
                flag = False

    if res == 'NO' or flag:
        break

print(res)
