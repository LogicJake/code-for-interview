def function(N, x):
    m = len(N)

    def help(start, reset_num):
        min_c = '9'
        min_index = 0
        for i in range(start, len(N)):
            if N[i] < min_c and m - i - 1 >= reset_num:
                min_c = N[i]
                min_index = i
        return min_c, min_index

    result = []
    start = -1
    for i in range(m - x):
        start = start + 1
        a, start = help(start, m - x - i - 1)
        result.append(a)

    while result[0] == '0':
        result.pop(0)

    return ''.join(result)


print(function('2020', 1))
