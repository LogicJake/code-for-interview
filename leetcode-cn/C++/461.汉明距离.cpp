/*
 * @lc app=leetcode.cn id=461 lang=cpp
 *
 * [461] 汉明距离
 */

// @lc code=start
class Solution {
public:
    int hammingDistance(int x, int y)
    {
        int ans = 0;

        int s = x ^ y;

        while (s) {
            ans += s & 1;
            s >>= 1;
        }

        return ans;
    }
};
// @lc code=end
