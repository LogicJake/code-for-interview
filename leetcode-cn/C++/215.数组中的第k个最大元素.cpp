/*
 * @lc app=leetcode.cn id=215 lang=cpp
 *
 * [215] 数组中的第K个最大元素
 */

// @lc code=start
#include <stdlib.h>
#include <vector>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k, int left, int right)
    {
        int i = rand() % (right - left + 1) + left;
        swap(nums[i], nums[left]);

        int p = left;
        int q = right;
        int privot = nums[left];

        while (p < q) {
            while (p < q && nums[q] >= privot) {
                q--;
            }
            nums[p] = nums[q];

            while (p < q && nums[p] <= privot) {
                p++;
            }
            nums[q] = nums[p];
        }

        if (p == k) {
            return privot;
        } else if (p < k) {
            return findKthLargest(nums, k, p + 1, right);
        } else {
            return findKthLargest(nums, k, left, p - 1);
        }
    }

    int findKthLargest(vector<int>& nums, int k)
    {
        return findKthLargest(nums, nums.size() - k, 0, nums.size() - 1);
    }
};
// @lc code=end
