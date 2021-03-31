expect = [33, 66, 99]
remain = [3, 6, 9, 30, 60, 90]

bucket_cnt = [0] * 10
buckets = [[] for _ in range(10)]

for num in remain:
    bucket_cnt[num // 10] += 1
    buckets[num // 10].append(num)

ans = []
for num in expect:
    cnt = sum(bucket_cnt[num // 10 + 1:10])

    for i in buckets[num // 10]:
        if i >= num:
            cnt += 1
    ans.append(cnt)

print(ans)
