/*
 * @lc app=leetcode.cn id=5755 lang=cpp
 *
 * [5755] 数组中最大数对和的最小值
 */

// @lc code=start
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int minPairSum(vector<int>& nums)
    {
        int n = nums.size();
        int res = 0;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n / 2; ++i) {
            res = max(res, nums[i] + nums[n - 1 - i]);
        }
        return res;
    }
};
// @lc code=end
