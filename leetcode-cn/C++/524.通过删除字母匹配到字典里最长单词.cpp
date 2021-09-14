/*
 * @lc app=leetcode.cn id=524 lang=cpp
 *
 * [524] 通过删除字母匹配到字典里最长单词
 */

// @lc code=start
#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    string findLongestWord(string s, vector<string> &dictionary)
    {
        string res = "";

        for (string t : dictionary)
        {
            int i = 0;
            int j = 0;

            while (i < s.size() && j < t.size())
            {
                if (s[i] == t[j])
                {
                    j++;
                }
                i++;
            }

            if (j == t.size())
            {
                if (t.size() > res.size() || (t.size() == res.size() && t < res))
                {
                    res = t;
                }
            }
        }

        return res;
    }
};
// @lc code=end
