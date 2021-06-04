/*
 * @lc app=leetcode.cn id=43 lang=cpp
 *
 * [43] 字符串相乘
 */

// @lc code=start
#include <algorithm>
#include <string>

using namespace std;

class Solution {
public:
    string addStrings(string& num1, string& num2)
    {
        int i = num1.size() - 1, j = num2.size() - 1, add = 0;
        string ans;
        while (i >= 0 || j >= 0 || add != 0) {
            int x = i >= 0 ? num1[i] - '0' : 0;
            int y = j >= 0 ? num2[j] - '0' : 0;
            int result = x + y + add;

            add = result / 10;
            result = result % 10;
            ans.push_back(result + '0');
            i--;
            j--;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }

    string multiply(string num1, string num2)
    {

        if (num1 == "0" || num2 == "0") {
            return "0";
        }

        int m = num1.length();
        int n = num2.length();

        string ans = "0";

        for (int i = n - 1; i >= 0; i--) {
            string curr;

            // 结果先补0
            for (int j = 0; j < n - 1 - i; j++) {
                curr.push_back('0');
            }

            // 做乘法
            int add = 0;
            int y = num2[i] - '0';
            for (int j = m - 1; j >= 0; j--) {
                int x = num1[j] - '0';
                int product = x * y + add;
                add = product / 10;
                product = product % 10;
                curr.push_back(product + '0');
            }

            while (add != 0) {
                curr.push_back((add % 10) + '0');
                add /= 10;
            }
            reverse(curr.begin(), curr.end());
            ans = addStrings(ans, curr);
        }

        return ans;
    }
};
// @lc code=end
