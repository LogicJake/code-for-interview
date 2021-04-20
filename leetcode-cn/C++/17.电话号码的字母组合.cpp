/*
 * @lc app=leetcode.cn id=17 lang=cpp
 *
 * [17] 电话号码的字母组合
 */

// @lc code=start
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;
class Solution {
public:
    vector<string> ans;
    string path = "";
    unordered_map<char, string> map = {
        { '2', "abc" },
        { '3', "def" },
        { '4', "ghi" },
        { '5', "jkl" },
        { '6', "mno" },
        { '7', "pqrs" },
        { '8', "tuv" },
        { '9', "wxyz" }
    };

    void help(const string digits, int index)
    {
        if (index == digits.size()) {
            ans.push_back(path);
        }

        string chars = map[digits[index]];
        for (char c : chars) {
            path += c;
            help(digits, index + 1);
            path.pop_back();
        }
    }

    vector<string> letterCombinations(string digits)
    {
        if (digits.size() == 0) {
            return {};
        }

        help(digits, 0);
        return ans;
    }
};
// @lc code=end
