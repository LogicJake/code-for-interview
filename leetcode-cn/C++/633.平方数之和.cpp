/*
 * @lc app=leetcode.cn id=633 lang=cpp
 *
 * [633] 平方数之和
 */

// @lc code=start
#include <math.h>
using namespace std;
class Solution {
public:
    bool judgeSquareSum(int c)
    {
        long left = 0;
        long right = sqrt(c);

        while (left <= right) {
            long sum = left * left + right * right;
            if (sum == c) {
                return true;
            } else if (sum < c) {
                left++;
            } else {
                right--;
            }
        }
        return false;
    }
};
// @lc code=end
