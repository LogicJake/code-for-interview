nums = ['a', 'ppap', 'ap', 'aaappa', 'p']
num_a = 2
num_p = 3

new_nums = []
for num in nums:
    new_nums.append([num.count('a'), num.count('p')])

nums = new_nums

ans = 0
path = []


def help(index):
    global ans
    num_0 = sum([i[0] for i in path])
    num_1 = sum([i[1] for i in path])

    if num_0 <= num_a and num_1 <= num_p:
        ans = max(ans, len(path))
    else:
        return

    for i in range(index, len(nums)):
        path.append(nums[i])
        help(i + 1)
        path.pop(-1)


help(0)
print(ans)
