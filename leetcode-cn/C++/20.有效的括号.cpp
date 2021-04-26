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

class Solution {
public:
    bool isValid(string s)
    {
        unordered_map<char, char> pairs = {
            { ')', '(' },
            { ']', '[' },
            { '}', '{' }
        };

        stack<char> st;

        for (char c : s) {
            if (pairs.count(c)) {
                if (st.empty() || st.top() != pairs[c]) {
                    return false;
                }
                st.pop();

            } else {
                st.push(c);
            }
        }

        return st.empty();
    }
};
// @lc code=end
