/*
 * @lc app=leetcode.cn id=1711 lang=cpp
 *
 * [1711] 大餐计数
 */

// @lc code=start
#include <vector>
#include <unordered_map>
using namespace std;

class Solution
{
public:
    static constexpr int MOD = 1000000007;

    int countPairs(vector<int> &deliciousness)
    {
        int maxVal = *max_element(deliciousness.begin(), deliciousness.end());
        int maxSum = maxVal * 2;
        int pairs = 0;
        unordered_map<int, int> mp;
        int n = deliciousness.size();
        for (auto &val : deliciousness)
        {
            for (int sum = 1; sum <= maxSum; sum <<= 1)
            {
                int count = mp.count(sum - val) ? mp[sum - val] : 0;
                pairs = (pairs + count) % MOD;
            }
            mp[val]++;
        }
        return pairs;
    }
};

// @lc code=end
