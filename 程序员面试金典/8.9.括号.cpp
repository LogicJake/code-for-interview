#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> ans;
    string tmp;

    // n 剩余可用括号对，left 未配对的左括号数量
    void dfs(int n, int left)
    {
        if (n == 0 && left == 0) {
            ans.push_back(tmp);
            return;
        }

        if (n) {
            tmp.push_back('(');
            dfs(n - 1, left + 1);
            tmp.pop_back();
        }

        if (left) {
            tmp.push_back(')');
            dfs(n, left - 1);
            tmp.pop_back();
        }
    }

    vector<string> generateParenthesis(int n)
    {
        dfs(n, 0);
        return ans;
    }
};