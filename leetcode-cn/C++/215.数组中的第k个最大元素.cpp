/*
 * @lc app=leetcode.cn id=215 lang=cpp
 *
 * [215] 数组中的第K个最大元素
 */

// @lc code=start
#include <queue>
#include <stdlib.h>
#include <vector>

using namespace std;

class Solution {
public:
    int quickSelect(vector<int>& nums, int left, int right, int target)
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

            while (p < q && nums[p] < privot) {
                p++;
            }
            nums[q] = nums[p];
        }

        if (p == target) {
            return privot;
        } else if (p > target) {
            return quickSelect(nums, left, p - 1, target);
        } else {
            return quickSelect(nums, p + 1, right, target);
        }
    }

    int findKthLargest(vector<int>& nums, int k)
    {
        return quickSelect(nums, 0, nums.size() - 1, nums.size() - k);
    }
};
// @lc code=end
