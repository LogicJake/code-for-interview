/*
 * @lc app=leetcode.cn id=1833 lang=cpp
 *
 * [1833] 雪糕的最大数量
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution
{
public:
    int maxIceCream(vector<int> &costs, int coins)
    {
        sort(costs.begin(), costs.end());
        int count = 0;
        int n = costs.size();
        for (int i = 0; i < n; i++)
        {
            int cost = costs[i];
            if (coins >= cost)
            {
                coins -= cost;
                count++;
            }
            else
            {
                break;
            }
        }
        return count;
    }
};
// @lc code=end
