/*
 * @lc app=leetcode.cn id=53 lang=cpp
 *
 * [53] 最大子序和
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums)
    {
        int ans = nums[0];

        int tmp = 0;

        for (int i = 0; i < nums.size(); i++) {
            tmp = max(nums[i], tmp + nums[i]);
            ans = max(ans, tmp);
        }

        return ans;
    }
};
// @lc code=end
