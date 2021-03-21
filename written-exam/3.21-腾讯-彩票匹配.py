line = input()
n, m = line.split(' ')
n = int(n)
m = int(m)

line = input()
a = line.split(' ')
a = [int(i) for i in a]

line = input()
b = line.split(' ')
b = [int(i) for i in b]

total = 0
ans = []
for num in a:
    if num in b:
        ans.append(str(num))
        total += num
print(' '.join(ans))
print(total)
