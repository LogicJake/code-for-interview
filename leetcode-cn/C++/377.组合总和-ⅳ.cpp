/*
 * @lc app=leetcode.cn id=377 lang=cpp
 *
 * [377] 组合总和 Ⅳ
 */

// @lc code=start
#include <limits.h>
#include <vector>

using namespace std;
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target)
    {
        vector<int> dp(target + 1);
        dp[0] = 1;

        for (int i = 1; i <= target; i++) {
            for (int num : nums) {
                if (num <= i && dp[i - num] < INT_MAX - dp[i]) {
                    dp[i] += dp[i - num];
                }
            }
        }
        return dp[target];
    }
};
// @lc code=end
