def lcm(nums):
    ans = max(nums)
    while 1:
        if len(list(filter(lambda i: ans % i != 0, nums))) == 0:
            return ans
        ans += 1


def help(n, x_list, y_list):
    a = lcm(y_list)

    x_total = 0

    for i in range(n):
        tmp = a // y_list[i]
        x_total += x_list[i] * tmp

    if x_total % a == 0:
        print('Yes')
    else:
        print('No')


help(4, [1, 3, 5, 7], [2, 4, 6, 8])
