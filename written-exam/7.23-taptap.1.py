# 输入一个整数序列，判断这个序列是否有可能是一棵严格的二叉查找树从根节点到叶子结点的路径。例如序列5, 3, 8不可能满足条件。

def isValid(nums):
    if len(nums) == 1:
        return True

    max_ = nums[-1]
    min_ = nums[-1]

    for i in range(len(nums)-1, -1, -1):
        # 更新从当前数往后的最大值和最小值
        max_ = max(max_, nums[i])
        min_ = min(min_, nums[i])

        # i 不是第一个数字
        if i - 1 >= 0:
            # 当前节点在上一个节点的右子树
            if nums[i] > nums[i-1]:
                # 所有元素都应该比根结点数值大
                if min_ < nums[i-1]:
                    return False
            else:
                # 所有元素都应该比根结点数值小
                if max_ > nums[i-1]:
                    return False

    return True

nums = [5, 3, 4]
ans = isValid(nums)
print(ans)
