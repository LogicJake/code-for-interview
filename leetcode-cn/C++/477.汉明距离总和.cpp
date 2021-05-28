/*
 * @lc app=leetcode.cn id=477 lang=cpp
 *
 * [477] 汉明距离总和
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    int totalHammingDistance(vector<int>& nums)
    {
        int n = nums.size();
        int ans = 0;

        for (int i = 0; i < 32; i++) {
            int s = 0;

            for (int num : nums) {
                if ((num >> i) & 1 == 1) {
                    s++;
                }
            }

            ans += s * (n - s);
        }

        return ans;
    }
};
// @lc code=end
