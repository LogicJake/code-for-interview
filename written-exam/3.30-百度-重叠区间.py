m = 2

requires = [[[4, 5], [8, 8], [1, 2]], [[1, 4], [3, 8]]]


def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


# source 区间列表和 target 区间列表的重复区间
def intervalIntersection(A, B):
    ans = []
    i = j = 0

    while i < len(A) and j < len(B):
        # Let's check if A[i] intersects B[j].
        # lo - the startpoint of the intersection
        # hi - the endpoint of the intersection
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])
        if lo <= hi:
            ans.append([lo, hi])

        # Remove the interval with the smallest endpoint
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1

    return ans


new_requires = []

for require in requires:
    merged = merge(require)
    new_requires.append(merged)

source = new_requires[0]
for i in range(1, m):
    source = intervalIntersection(source, new_requires[i])

ans = []
for s in source:
    for i in range(s[0], s[1] + 1):
        ans.append(str(i))

print(len(ans))
print(' '.join(ans))
