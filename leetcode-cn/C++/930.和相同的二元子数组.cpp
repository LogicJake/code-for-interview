/*
 * @lc app=leetcode.cn id=930 lang=cpp
 *
 * [930] 和相同的二元子数组
 */

// @lc code=start
#include <vector>
#include <unordered_map>
using namespace std;

class Solution
{
public:
    int numSubarraysWithSum(vector<int> &nums, int goal)
    {

        unordered_map<int, int> cnt;
        int ans = 0;
        int pre = 0;

        for (int num : nums)
        {
            cnt[pre]++;
            pre += num;
            ans += cnt[pre - goal];
        }

        return ans;
    }
};
// @lc code=end
