/*
 * @lc app=leetcode.cn id=645 lang=cpp
 *
 * [645] 错误的集合
 */

// @lc code=start
#include <vector>
#include <unordered_map>
using namespace std;

class Solution
{
public:
    vector<int> findErrorNums(vector<int> &nums)
    {
        vector<int> ans(2, 0);
        unordered_map<int, int> cnt;

        for (int num : nums)
        {
            cnt[num]++;
        }

        for (int i = 1; i < nums.size() + 1; i++)
        {
            if (cnt[i] == 2)
            {
                ans[0] = i;
            }

            if (cnt[i] == 0)
            {
                ans[1] = i;
            }
        }

        return ans;
    }
};
// @lc code=end
