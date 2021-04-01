#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    /**
     * 反转字符串
     * @param str string字符串 
     * @return string字符串
     */
    string solve(string str)
    {
        stack<char> st;
        for (int i = 0; i < str.size(); i++) {
            st.push(str[i]);
        }

        string ans;

        while (!st.empty()) {
            ans += st.top();
            st.pop();
        }

        return ans;
    }
};