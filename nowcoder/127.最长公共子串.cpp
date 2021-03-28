#include <string>
using namespace std;
class Solution {
public:
    /**
     * longest common substring
     * @param str1 string字符串 the string
     * @param str2 string字符串 the string
     * @return string字符串
     */
    string LCS(string str1, string str2)
    {
        int len1 = str1.size();
        int len2 = str2.size();

        int dp[len1 + 1][len2 + 1];
        int ans = 0, end = 0;

        for (int i = 0; i <= len1; ++i)
            dp[i][0] = 0;
        for (int j = 0; j <= len2; ++j)
            dp[0][j] = 0;

        for (int i = 1; i <= len1; ++i) {
            for (int j = 1; j <= len2; ++j) {
                if (str1[i - 1] == str2[j - 1])
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                else
                    dp[i][j] = 0;
                if (dp[i][j] > ans) {
                    ans = dp[i][j];
                    end = j - 1;
                }
            }
        }

        string r;
        if (ans == 0)
            return "-1";
        else
            r = str2.substr(end - ans + 1, ans);
        return r;
    }
};