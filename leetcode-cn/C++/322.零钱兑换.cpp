/*
 * @lc app=leetcode.cn id=322 lang=cpp
 *
 * [322] 零钱兑换
 */

// @lc code=start
#include <vector>

using namespace std;

class Solution
{
public:
    int coinChange(vector<int> &coins, int amount)
    {
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0;

        for (int coin : coins)
        {
            for (int i = 1; i < amount + 1; i++)
            {
                if (i - coin >= 0)
                {
                    dp[i] = min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        if (dp[amount] == amount + 1)
        {
            return -1;
        }
        else
        {
            return dp[amount];
        }
    }
};
// @lc code=end
