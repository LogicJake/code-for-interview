#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int countEval(string s, int result)
    {
        if (s.length() == 0) {
            return 0;
        }
        if (s.length() == 1) {
            return (s[0] - '0') == result ? 1 : 0;
        }

        int m = s.length();
        vector<vector<vector<int>>> dp(m, vector<vector<int>>(m, vector<int>(2)));

        for (int i = 0; i < m; i++) {
            if (s[i] == '0' || s[i] == '1') {
                dp[i][i][s[i] - '0'] = 1;
            }
        }

        for (int len = 2; len < m; len += 2) {
            for (int i = 0; i < m - len; i += 2) {
                int j = i + len;
                for (int k = i + 1; k < j; k += 2) {
                    if (s[k] == '&') {
                        //结果为0 有三种情况： 0 0, 0 1, 1 0
                        //结果为1 有一种情况： 1 1
                        dp[i][j][0] += dp[i][k - 1][0] * dp[k + 1][j][0] + dp[i][k - 1][0] * dp[k + 1][j][1] + dp[i][k - 1][1] * dp[k + 1][j][0];
                        dp[i][j][1] += dp[i][k - 1][1] * dp[k + 1][j][1];
                    }
                    if (s[k] == '|') {
                        //结果为0 有一种情况： 0 0
                        //结果为1 有三种情况： 0 1, 1 0, 1 1
                        dp[i][j][0] += dp[i][k - 1][0] * dp[k + 1][j][0];
                        dp[i][j][1] += dp[i][k - 1][0] * dp[k + 1][j][1] + dp[i][k - 1][1] * dp[k + 1][j][0] + dp[i][k - 1][1] * dp[k + 1][j][1];
                    }
                    if (s[k] == '^') {
                        //结果为0 有两种情况： 0 0, 1 1
                        //结果为1 有两种情况： 0 1, 1 0
                        dp[i][j][0] += dp[i][k - 1][0] * dp[k + 1][j][0] + dp[i][k - 1][1] * dp[k + 1][j][1];
                        dp[i][j][1] += dp[i][k - 1][1] * dp[k + 1][j][0] + dp[i][k - 1][0] * dp[k + 1][j][1];
                    }
                }
            }
        }

        return dp[0][m - 1][result];
    }
};