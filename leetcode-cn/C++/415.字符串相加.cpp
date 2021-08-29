/*
 * @lc app=leetcode.cn id=415 lang=cpp
 *
 * [415] 字符串相加
 */

// @lc code=start
#include <string>
using namespace std;

class Solution
{
public:
    string addStrings(string num1, string num2)
    {
        int i = num1.size() - 1;
        int j = num2.size() - 1;
        int add = 0;

        string ans;
        while (i >= 0 || j >= 0 || add)
        {
            int x = 0;
            int y = 0;
            if (i >= 0)
            {
                x = num1[i] - '0';
            }
            if (j >= 0)
            {
                y = num2[j] - '0';
            }
            int result = x + y + add;
            ans.push_back('0' + result % 10);
            add = result / 10;

            i -= 1;
            j -= 1;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
// @lc code=end
