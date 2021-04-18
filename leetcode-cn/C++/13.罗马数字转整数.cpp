/*
 * @lc app=leetcode.cn id=13 lang=cpp
 *
 * [13] 罗马数字转整数
 */

// @lc code=start
#include <string>
using namespace std;
class Solution {
public:
    int getValue(char c)
    {

        switch (c) {
        case 'I':
            return 1;
        case 'V':
            return 5;
        case 'X':
            return 10;
        case 'L':
            return 50;
        case 'C':
            return 100;
        case 'D':
            return 500;
        case 'M':
            return 1000;
        default:
            return 0;
        }
    }

    int romanToInt(string s)
    {
        int pre_value = getValue(s[0]);
        int ans = 0;
        for (int i = 1; i < s.size(); i++) {
            int num = getValue(s[i]);
            if (num <= pre_value) {
                ans += pre_value;
            } else {
                ans -= pre_value;
            }
            pre_value = num;
        }
        ans += pre_value;
        return ans;
    }
};
// @lc code=end
