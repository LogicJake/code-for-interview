class Solution {
public:
    int fib(int n)
    {
        if (n <= 1) {
            return n;
        }

        int ans = 0;
        int pre1 = 0;
        int pre2 = 1;

        for (int i = 2; i <= n; i++) {
            ans = (pre1 + pre2) % 1000000007;

            pre1 = pre2;
            pre2 = ans;
        }

        return ans % 1000000007;
    }
};