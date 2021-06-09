#include <vector>
using namespace std;

class Solution {
public:
    int waysToChange(int n)
    {
        int MOD = 1000000007;
        int weights[] = { 25, 10, 5, 1 };
        int m = 4;
        vector<int> dp(n + 1);

        dp[0] = 1;

        for (int i = 1; i <= m; i++) {
            int weight = weights[i - 1];
            for (int j = 1; j <= n; j++) {
                if (weight > j) {
                    dp[j] = dp[j];
                } else {
                    dp[j] = (dp[j] + dp[j - weight]) % MOD;
                }
            }
        }
        return dp[n] % MOD;
    }
};