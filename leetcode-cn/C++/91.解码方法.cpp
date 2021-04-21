/*
 * @lc app=leetcode.cn id=91 lang=cpp
 *
 * [91] 解码方法
 */

// @lc code=start
#include <iostream>
#include <string.h>
#include <string>

using namespace std;

class Solution {
public:
    int numDecodings(string s)
    {
        int n = s.size();

        if (n == 0) {
            return 0;
        }

        int dp[n];
        memset(dp, 0, sizeof(dp));

        for (int i = 0; i < n; i++) {
            if (s[i] != '0') {
                if (i - 1 >= 0) {
                    dp[i] += dp[i - 1];
                } else {
                    dp[i] += 1;
                }
            }

            if (i - 1 >= 0 && s[i - 1] != '0' && (s[i - 1] - '0') * 10 + (s[i] - '0') <= 26) {
                if (i - 2 >= 0) {
                    dp[i] += dp[i - 2];
                } else {
                    dp[i] += 1;
                }
            }
        }

        return dp[n - 1];
    }
};
// @lc code=end
