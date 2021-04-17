/*
 * @lc app=leetcode.cn id=12 lang=cpp
 *
 * [12] 整数转罗马数字
 */

// @lc code=start
#include <string>
using namespace std;
class Solution {
public:
    string intToRoman(int num)
    {
        string strs[] = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
        int nums[] = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };

        string ans = "";
        for (int i = 0; i < 13; i++) {
            if (num == 0) {
                break;
            }
            while (num >= nums[i]) {
                ans += strs[i];
                num -= nums[i];
            }
        }
        return ans;
    }
};
// @lc code=end
