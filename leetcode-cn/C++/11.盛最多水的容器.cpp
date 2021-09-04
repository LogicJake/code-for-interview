/*
 * @lc app=leetcode.cn id=11 lang=cpp
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int left = 0;
        int right = height.size() - 1;
        int ans = 0;

        while (left < right)
        {
            ans = max(ans, min(height[left], height[right]) * (right - left));

            if (height[left] < height[right])
            {
                left++;
            }
            else
            {
                right--;
            }
        }

        return ans;
    }
};
// @lc code=end
