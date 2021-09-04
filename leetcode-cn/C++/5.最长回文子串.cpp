/*
 * @lc app=leetcode.cn id=5 lang=cpp
 *
 * [5] 最长回文子串
 */

// @lc code=start
#include <string>
#include <vector>
using namespace std;

class Solution
{
public:
    string longestPalindrome(string s)
    {
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n, false));

        for (int i = 0; i < n; i++)
        {
            dp[i][i] = true;
        }

        int start = 0;
        int end = 0;

        for (int len = 2; len <= n; len++)
        {
            for (int i = 0; i < n; i++)
            {
                int j = i + len - 1;
                if (j >= n)
                {
                    break;
                }

                if (s[i] == s[j])
                {
                    if (len == 2 || (i + 1 <= j - 1 && dp[i + 1][j - 1]))
                    {
                        dp[i][j] = true;
                    }
                }

                if (dp[i][j] && j - i > end - start)
                {
                    start = i;
                    end = j;
                }
            }
        }
        return s.substr(start, end - start + 1);
    }
};
// @lc code=end
