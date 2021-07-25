T = input()
T = int(T)


def fun(a, b, c, q):
    visited = set()

    ans = 0

    def help(num):
        nonlocal ans, q
        if num == q:
            ans = 1
            return

        if num in visited or num > q:
            return

        visited.add(num)
        help(num + b)

        if ans == 1:
            return

        help(num * c)

    help(a)

    print(ans)


for _ in range(T):
    line = input()
    A, B, C, Q = line.split(' ')
    A = int(A)
    B = int(B)
    C = int(C)
    Q = int(Q)

    fun(A, B, C, Q)
