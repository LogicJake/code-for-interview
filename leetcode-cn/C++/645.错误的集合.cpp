/*
 * @lc app=leetcode.cn id=645 lang=cpp
 *
 * [645] 错误的集合
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> findErrorNums(vector<int> &nums)
    {
        vector<int> ans(2, 0);
        sort(nums.begin(), nums.end());

        int prev = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            int cur = nums[i];

            if (cur == prev)
            {
                ans[0] = cur;
            }

            if (cur - prev > 1)
            {
                ans[1] = prev + 1;
            }

            prev = cur;
        }

        if (nums[nums.size() - 1] != nums.size())
        {
            ans[1] = nums.size();
        }

        return ans;
    }
};
// @lc code=end
