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
        vector<vector<bool>> dp(n, vector<bool>(n));
        int start = 0;
        int end = 0;

        for (int len = 1; len <= s.size(); len++)
        {
            for (int i = 0; i < s.size(); i++)
            {
                int j = i + len - 1;
                if (j >= s.size())
                {
                    break;
                }

                if (s[i] == s[j])
                {
                    if (j - i < 3)
                    {
                        dp[i][j] = true;
                    }
                    else
                    {
                        dp[i][j] = dp[i + 1][j - 1];
                    }
                }
                else
                {
                    dp[i][j] = false;
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
