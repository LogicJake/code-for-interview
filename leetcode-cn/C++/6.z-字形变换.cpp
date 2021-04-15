/*
 * @lc app=leetcode.cn id=6 lang=cpp
 *
 * [6] Z 字形变换
 */

// @lc code=start
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows)
    {
        if (numRows == 1) {
            return s;
        }

        vector<string> mem(min(numRows, int(s.size())));
        int cur = 0;
        bool flag = false;

        for (char c : s) {
            mem[cur] += c;
            if (cur == 0 || cur == numRows - 1) {
                flag = !flag;
            }
            if (flag) {
                cur++;
            } else {
                cur--;
            }
        }

        string ans;
        for (string row : mem) {
            ans += row;
        }
        return ans;
    }
};
// @lc code=end
