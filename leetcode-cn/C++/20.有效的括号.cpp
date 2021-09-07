/*
 * @lc app=leetcode.cn id=20 lang=cpp
 *
 * [20] 有效的括号
 */

// @lc code=start
#include <stack>
#include <string>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    bool isValid(string s)
    {
        unordered_map<char, char> map = {
            {')', '('},
            {'}', '{'},
            {']', '['},
        };
        stack<char> st;

        for (char c : s)
        {
            if (c == '(' || c == '{' || c == '[')
            {
                st.push(c);
            }
            else
            {
                if (st.empty() || map[c] != st.top())
                {
                    return false;
                }
                st.pop();
            }
        }

        if (st.empty())
        {
            return true;
        }

        return false;
    }
};
// @lc code=end
