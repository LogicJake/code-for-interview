/*
 * @lc app=leetcode.cn id=14 lang=cpp
 *
 * [14] 最长公共前缀
 */

// @lc code=start
#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    string help(const string str1, const string str2)
    {
        int i = 0;
        for (; i < str1.size() && i < str2.size(); i++) {
            if (str1[i] != str2[i]) {
                break;
            }
        }
        return str1.substr(0, i);
    }

    string longestCommonPrefix(vector<string>& strs)
    {
        if (strs.size() == 0) {
            return "";
        }

        string prefix = strs[0];
        for (int i = 1; i < strs.size(); i++) {
            prefix = help(prefix, strs[i]);
            if (prefix.size() == 0) {
                break;
            }
        }
        return prefix;
    }
};
// @lc code=end
