/*
 * @lc app=leetcode.cn id=55 lang=cpp
 *
 * [55] 跳跃游戏
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution
{
public:
    bool canJump(vector<int> &nums)
    {
        int max_ = 0;
        int n = nums.size();

        for (int i = 0; i < n; i++)
        {
            if (i <= max_)
            {
                max_ = max(max_, i + nums[i]);
                if (max_ >= n - 1)
                {
                    return true;
                }
            }
        }
        return false;
    }
};
// @lc code=end
