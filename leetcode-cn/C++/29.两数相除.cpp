/*
 * @lc app=leetcode.cn id=29 lang=cpp
 *
 * [29] 两数相除
 */

// @lc code=start
#include <limits.h>

class Solution {
public:
    int divide(int dividend, int divisor)
    {
        if (dividend == 0) {
            return 0;
        }
        if (divisor == 1) {
            return dividend;
        }
        if (divisor == -1) {
            if (dividend > INT_MIN) {
                return -dividend;
            } else {
                return INT_MAX;
            }
        }

        int sign = 1;
        if ((dividend > 0 && divisor < 0) || (dividend < 0 && divisor > 0)) {
            sign = -1;
        }

        long a = dividend;
        a = a > 0 ? a : -a;
        long b = divisor;
        b = b > 0 ? b : -b;

        long res = div(a, b);
        if (sign > 0)
            return res > INT_MAX ? INT_MAX : res;
        return -res;
    }

    long div(long a, long b)
    {
        if (a < b)
            return 0;
        long count = 1;
        long tb = b;
        while ((tb + tb) <= a) {
            count = count + count;
            tb = tb + tb;
        }
        return count + div(a - tb, b);
    }
};
// @lc code=end
