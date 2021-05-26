/*
 * @lc app=leetcode.cn id=1190 lang=cpp
 *
 * [1190] 反转每对括号间的子串
 */

// @lc code=start
#include <algorithm>
#include <stack>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string reverseParentheses(string s)
    {
        stack<char> st;
        for (char c : s) {
            if (c == ')') {
                vector<char> tmp;
                while (!st.empty() && st.top() != '(') {
                    tmp.push_back(st.top());
                    st.pop();
                }
                st.pop();

                for (char c2 : tmp) {
                    st.push(c2);
                }
            } else {
                st.push(c);
            }
        }

        string ans = "";
        while (!st.empty()) {
            ans += st.top();
            st.pop();
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
// @lc code=end
