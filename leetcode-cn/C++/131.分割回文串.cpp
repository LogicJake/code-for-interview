/*
 * @lc app=leetcode.cn id=131 lang=cpp
 *
 * [131] 分割回文串
 */

// @lc code=start
#include <vector>
#include <string>
using namespace std;

class Solution
{
public:
    int n = 0;
    vector<vector<int>> f;
    vector<vector<string>> ans;
    vector<string> tmp;
    string s;

    void dfs(int i)
    {
        if (i == n)
        {
            ans.push_back(tmp);
            return;
        }

        for (int j = i; j < n; j++)
        {
            if (f[i][j])
            {
                tmp.push_back(s.substr(i, j - i + 1));
                dfs(j + 1);
                tmp.pop_back();
            }
        }
    }

    vector<vector<string>> partition(string s)
    {
        n = s.size();
        f.assign(n, vector<int>(n, true));
        this->s = s;

        for (int i = n - 1; i >= 0; i--)
        {
            for (int j = i + 1; j < n; j++)
            {
                f[i][j] = ((s[i] == s[j]) && f[i + 1][j - 1]);
            }
        }
        dfs(0);
        return ans;
    }
};
// @lc code=end
