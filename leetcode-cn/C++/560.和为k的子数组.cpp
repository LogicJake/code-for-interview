/*
 * @lc app=leetcode.cn id=560 lang=cpp
 *
 * [560] 和为K的子数组
 */

// @lc code=start
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k)
    {
        int n = nums.size();
        vector<int> mem(n + 1, 0);
        for (int i = 0; i < n; i++) {
            mem[i + 1] = mem[i] + nums[i];
        }

        unordered_map<int, int> map;
        int ans = 0;

        for (int i = 0; i < n + 1; i++) {
            if (map.find(mem[i] - k) != map.end()) {
                ans += map[mem[i] - k];
            }
            map[mem[i]]++;
        }

        return ans;
    }
};
// @lc code=end
