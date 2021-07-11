/*
 * @lc app=leetcode.cn id=274 lang=cpp
 *
 * [274] H 指数
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution
{
public:
    int hIndex(vector<int> &citations)
    {
        int n = citations.size();
        vector<int> cnt(n + 1, 0);

        for (int citation : citations)
        {
            if (citation > n)
            {
                cnt[n]++;
            }
            else
            {
                cnt[citation]++;
            }
        }

        int total = 0;

        for (int i = n; i >= 0; i--)
        {
            total += cnt[i];
            if (total >= i)
            {
                return i;
            }
        }
        return 0;
    }
};
// @lc code=end
