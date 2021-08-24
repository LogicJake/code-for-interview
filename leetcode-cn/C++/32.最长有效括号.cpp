/*
 * @lc app=leetcode.cn id=32 lang=cpp
 *
 * [32] 最长有效括号
 */

// @lc code=start
#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    int longestValidParentheses(string s)
    {
        int n = s.size();
        int ans = 0;

        vector<int> dp(n, 0);

        for (int i = 0; i < n; i++)
        {
            if (s[i] == ')')
            {
                if (i - 1 >= 0)
                {
                    if (s[i - 1] == '(')
                    {
                        if (i - 2 >= 0)
                        {
                            dp[i] = dp[i - 2] + 2;
                        }
                        else
                        {
                            dp[i] = 2;
                        }
                    }
                    else
                    {
                        if (i - dp[i - 1] - 1 >= 0 && s[i - dp[i - 1] - 1] == '(')
                        {
                            if (i - dp[i - 1] - 2 >= 0)
                            {
                                dp[i] = dp[i - dp[i - 1] - 2] + 2 + dp[i - 1];
                            }
                            else
                            {
                                dp[i] = 2 + dp[i - 1];
                            }
                        }
                    }
                }
            }
            ans = max(ans, dp[i]);
        }

        return ans;
    }
};
// @lc code=end
