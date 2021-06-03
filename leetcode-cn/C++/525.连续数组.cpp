/*
 * @lc app=leetcode.cn id=525 lang=cpp
 *
 * [525] 连续数组
 */

// @lc code=start
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int findMaxLength(vector<int>& nums)
    {
        unordered_map<int, int> mp;
        mp[0] = -1;

        int cnt = 0;
        int ans = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 1) {
                cnt++;
            } else {
                cnt--;
            }

            if (mp.count(cnt)) {
                ans = max(ans, i - mp[cnt]);
            } else {
                mp[cnt] = i;
            }
        }
        return ans;
    }
};
// @lc code=end
