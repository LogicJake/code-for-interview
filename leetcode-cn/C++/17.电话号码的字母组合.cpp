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
class Solution
{
public:
    vector<string> ans;
    string path = "";
    unordered_map<char, string> map = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}};

    void help(int index, int n, string digits)
    {
        if (index == n)
        {
            if (path != "")
            {
                ans.push_back(path);
            }

            return;
        }

        for (char c : map[digits[index]])
        {
            path.push_back(c);
            help(index + 1, n, digits);
            path.pop_back();
        }
    }

    vector<string> letterCombinations(string digits)
    {
        help(0, digits.size(), digits);
        return ans;
    }
};
// @lc code=end
