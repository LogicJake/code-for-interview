/*
 * @lc app=leetcode.cn id=416 lang=cpp
 *
 * [416] 分割等和子集
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums)
    {
        int sum_ = 0;
        for (int num : nums) {
            sum_ += num;
        }

        if (sum_ % 2 != 0) {
            return false;
        }

        int target = sum_ / 2;
        int n = nums.size();
        vector<bool> dp(target + 1, false);

        if (nums[0] <= target) {
            dp[nums[0]] = true;
        }

        for (int i = 1; i < n; i++) {
            vector<bool> dpNext(target + 1, false);
            dpNext = dp;
            for (int j = 0; j < target + 1; j++) {
                if (j - nums[i] >= 0) {
                    dpNext[j] = dp[j] || dp[j - nums[i]];
                }
            }
            dp = dpNext;
        }
        return dp[target];
    }
};
// @lc code=end
