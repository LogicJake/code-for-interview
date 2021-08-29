/*
 * @lc app=leetcode.cn id=72 lang=cpp
 *
 * [72] 编辑距离
 */

// @lc code=start
#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    int minDistance(string word1, string word2)
    {
        int m = word1.size();
        int n = word2.size();

        if (m * n == 0)
        {
            return m + n;
        }

        vector<vector<int>> dp(m + 1, vector<int>(n + 1));

        for (int i = 0; i <= m; i++)
        {
            dp[i][0] = i;
        }
        for (int i = 0; i <= n; i++)
        {
            dp[0][i] = i;
        }

        for (int i = 1; i <= m; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                int p = dp[i - 1][j] + 1;
                int q = dp[i][j - 1] + 1;
                int r = dp[i - 1][j - 1];
                if (word1[i - 1] != word2[j - 1])
                {
                    r++;
                }
                dp[i][j] = min(p, min(q, r));
            }
        }
        return dp[m][n];
    }
};
// @lc code=end
