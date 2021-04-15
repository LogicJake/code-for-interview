N = int(input())
nums = []
for _ in range(N):
    num = int(input())
    nums.append(num)

ans = []
AEB_start = -1
AEB_end = -1
is_AEB = False
circle_start = 0
AEB_upload = [False] * N

for i, num in enumerate(nums):
    if circle_start % 60 == 0 and not is_AEB:
        ans.append(num)

    if i > 0 and nums[i - 1] - num >= 9:
        if AEB_start == -1:
            AEB_start = i
        else:
            AEB_end = i
            if AEB_end - AEB_start + 1 >= 4:
                is_AEB = True
                circle_start = 0
            # print(i, num, AEB_end, AEB_start)
    else:
        # 上报 AEB
        if is_AEB:
            for j in range(AEB_start - 4, AEB_start):
                if not AEB_upload[j]:
                    ans.append(nums[j])
                else:
                    AEB_upload[j] = True

            for j in range(AEB_start, AEB_end + 1):
                if not AEB_upload[j]:
                    ans.append(nums[j])
                else:
                    AEB_upload[j] = True

            for j in range(AEB_end + 1, AEB_end + 5):
                if not AEB_upload[j]:
                    ans.append(nums[j])
                else:
                    AEB_upload[j] = True
            # print(nums[AEB_start:AEB_end + 1])

            # 清空 AEB 数据
            AEB_start = -1
            AEB_end = -1
            is_AEB = False

    circle_start += 1

ans = map(str, ans)
print(','.join(ans))
