class Solution {
public:
    int multiply(int A, int B)
    {
        bool sign = true;
        if (A < 0) {
            sign = !sign;
            A = -A;
        }
        if (B < 0) {
            sign = !sign;
            B = -B;
        }

        int ans = 0;

        while (A) {
            if (A & 1 == 0) {
                ans += B;
                A--;
            } else {
                A >>= 1;
                B <<= 1;
            }
        }

        if (sign) {
            return ans;
        }
        return -ans;
    }
};