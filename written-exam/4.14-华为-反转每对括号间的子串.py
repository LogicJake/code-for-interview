s = '(u(love)i)'

stack = []

for c in s:
    if c != ')':
        stack.append(c)
    else:
        tmp = []

        while stack[-1] != '(':
            tmp.append(stack.pop(-1))

        stack.pop(-1)

        for c2 in tmp:
            stack.append(c2)

print(''.join(stack))
