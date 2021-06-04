/*
 * @lc app=leetcode.cn id=523 lang=cpp
 *
 * [523] 连续的子数组和
 */

// @lc code=start
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k)
    {
        unordered_map<int, int> mp;

        int n = nums.size();
        if (n < 2) {
            return false;
        }

        mp[0] = -1;
        int pre = 0;
        for (int i = 0; i < n; i++) {
            pre = pre + nums[i];
            if (mp.count(pre % k)) {
                if (i - mp[pre % k] >= 2) {
                    return true;
                }
            } else {
                mp[pre % k] = i;
            }
        }
        return false;
    }
};
// @lc code=end
