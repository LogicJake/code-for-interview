def help(s):
    ans = []
    num = 0
    flag = False

    for c in s:
        if c >= '0' and c <= '9':
            num = num * 10 + int(c)
            flag = True
        else:
            if flag:
                ans.append(num)
                num = 0
                flag = False

    if flag:
        ans.append(num)

    ans.sort()
    return ans


s = '0000100c0'
ans = help(s)
print(ans)
