/*
 * @lc app=leetcode.cn id=9 lang=cpp
 *
 * [9] 回文数
 */

// @lc code=start
class Solution {
public:
    bool isPalindrome(int x)
    {
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int reverseNum = 0;
        while (x > reverseNum) {
            reverseNum = reverseNum * 10 + x % 10;
            x /= 10;
        }

        return x == reverseNum / 10 || x == reverseNum;
    }
};
// @lc code=end
