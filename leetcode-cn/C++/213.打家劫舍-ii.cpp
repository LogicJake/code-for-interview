/*
 * @lc app=leetcode.cn id=213 lang=cpp
 *
 * [213] 打家劫舍 II
 */

// @lc code=start
#include <vector>
using namespace std;
class Solution {
public:
    int robRange(const vector<int> nums, int start, int end)
    {
        int first = nums[start];
        int second = max(nums[start], nums[start + 1]);

        for (int i = start + 2; i <= end; i++) {
            int tmp = second;
            second = max(second, first + nums[i]);
            first = tmp;
        }

        return second;
    }

    int rob(vector<int>& nums)
    {
        int n = nums.size();
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return nums[0];
        }
        if (n == 2) {
            return max(nums[0], nums[1]);
        }

        return max(robRange(nums, 1, n - 1), robRange(nums, 0, n - 2));
    }
};
// @lc code=end
