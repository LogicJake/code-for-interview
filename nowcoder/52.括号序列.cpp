#include <iostream>
#include <map>
#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    /**
     * 
     * @param s string字符串 
     * @return bool布尔型
     */
    bool isValid(string s)
    {
        stack<char> st;
        map<char, char> pair;
        pair[')'] = '(';
        pair['}'] = '{';
        pair[']'] = '[';

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                st.push(s[i]);
            } else {
                if (!st.empty() && st.top() == pair[s[i]]) {
                    st.pop();
                } else {
                    return false;
                }
            }
        }

        if (st.empty()) {
            return true;
        }
        return false;
    }
};