/*
 * @lc app=leetcode.cn id=77 lang=cpp
 *
 * [77] 组合
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution
{
public:
    vector<vector<int>> ans;
    vector<int> path;
    int k = 0;
    int n = 0;

    void help(int index)
    {
        if (path.size() == k)
        {
            ans.push_back(path);
            return;
        }

        for (int i = index; i <= n; i++)
        {
            path.push_back(i);
            help(i + 1);
            path.pop_back();
        }
    }

    vector<vector<int>> combine(int n, int k)
    {
        this->k = k;
        this->n = n;
        help(1);
        return ans;
    }
};
// @lc code=end
