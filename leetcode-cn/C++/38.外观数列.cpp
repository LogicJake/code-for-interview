/*
 * @lc app=leetcode.cn id=38 lang=cpp
 *
 * [38] 外观数列
 */

// @lc code=start
#include <string>
using namespace std;

class Solution {
public:
    string countAndSay(int n)
    {
        if (n == 1) {
            return "1";
        }

        string preRet = countAndSay(n - 1);
        string ans = "";
        char pre = preRet[0];
        int cnt = 1;
        for (int i = 1; i < preRet.size(); i++) {
            if (preRet[i] == preRet[i - 1]) {
                cnt += 1;
            } else {
                ans = ans + to_string(cnt) + pre;
                pre = preRet[i];
                cnt = 1;
            }
        }

        ans = ans + to_string(cnt) + pre;
        return ans;
    }
};
// @lc code=end
