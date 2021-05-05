/*
 * @lc app=leetcode.cn id=740 lang=cpp
 *
 * [740] 删除并获得点数
 */

// @lc code=start
#include <vector>

using namespace std;

class Solution {
public:
    int deleteAndEarn(vector<int>& nums)
    {
        int maxNum = 0;
        for (int num : nums) {
            maxNum = max(maxNum, num);
        }

        vector<int> sum(maxNum + 1);
        for (int num : nums) {
            sum[num] += num;
        }

        vector<int> dp(maxNum + 1);
        dp[0] = sum[0];
        dp[1] = max(sum[0], sum[1]);

        for (int i = 2; i < maxNum + 1; i++) {
            dp[i] = max(sum[i] + dp[i - 2], dp[i - 1]);
        }
        return dp[maxNum];
    }
};
// @lc code=end
