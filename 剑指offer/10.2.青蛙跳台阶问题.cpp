class Solution {
public:
    int numWays(int n)
    {
        if (n <= 1) {
            return 1;
        }

        int ans = 0;
        int pre1 = 1;
        int pre2 = 1;

        for (int i = 2; i <= n; i++) {
            ans = (pre1 + pre2) % 1000000007;
            pre1 = pre2;
            pre2 = ans;
        }

        return ans;
    }
};