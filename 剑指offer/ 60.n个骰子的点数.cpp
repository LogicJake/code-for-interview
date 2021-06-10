#include <algorithm>
#include <vector>

using namespace std;
class Solution {
public:
    vector<double> dicesProbability(int n)
    {
        vector<vector<int>> dp(11, vector<int>(70));

        for (int i = 1; i <= 6; i++) {
            dp[1][i] = 1;
        }

        for (int i = 2; i <= n; i++) {
            for (int j = i; j <= 6 * i; j++) {
                for (int cur = 1; cur <= 6; cur++) {
                    if (j - cur <= 0) {
                        break;
                    }
                    dp[i][j] += dp[i - 1][j - cur];
                }
            }
        }

        vector<double> ans;

        for (int s = n; s <= 6 * n; s++) {
            ans.push_back(1.0 / pow(6, n) * dp[n][s]);
        }

        return ans;
    }
};