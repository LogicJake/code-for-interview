# N = 4
# nums1 = [1, 2, 3, 4]
# nums2 = [5, 6, 7, 8]

N = input()
N = int(N)

nums1 = input()
nums1 = nums1.split(' ')
nums1 = [int(i) for i in nums1]

nums2 = input()
nums2 = nums2.split(' ')
nums2 = [int(i) for i in nums2]

ans1 = 0
ans2 = 0

i = 0
j = 0

window = []

while i < N or j < N:
    # nums1 放牌
    while i < N and nums1[i] in window:
        while window[-1] != nums1[i]:
            window.pop(-1)
            ans1 += 1

        window.pop(-1)
        ans1 += 1

        ans1 += 1
        i += 1

    if i < N:
        window.append(nums1[i])
        i += 1

    # nums2 放牌
    while j < N and nums2[j] in window:
        while window[-1] != nums2[j]:
            window.pop(-1)
            ans2 += 1

        window.pop(-1)
        ans2 += 1

        ans2 += 1
        j += 1

    if j < N:
        window.append(nums2[j])
        j += 1

for num in window:
    if num % 2 == 0:
        ans2 += 1
    else:
        ans1 += 1

print(ans1, ans2)
