/*
 * @lc app=leetcode.cn id=22 lang=cpp
 *
 * [22] 括号生成
 */

// @lc code=start
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    void help(vector<string>& ans, string path, int left, int right, int n)
    {
        if (left == n && right == n) {
            ans.push_back(path);
            return;
        }
        if (left < n) {
            path.push_back('(');
            help(ans, path, left + 1, right, n);
            path.pop_back();
        }

        if (right < left) {
            path.push_back(')');
            help(ans, path, left, right + 1, n);
            path.pop_back();
        }
    }

    vector<string> generateParenthesis(int n)
    {
        vector<string> ans;
        string path;
        help(ans, path, 0, 0, n);
        return ans;
    }
};
// @lc code=end
