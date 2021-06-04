/*
 * @lc app=leetcode.cn id=40 lang=cpp
 *
 * [40] 组合总和 II
 */

// @lc code=start
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> path;
    vector<vector<int>> ans;
    vector<int> candidates;

    void help(int index, int target)
    {
        if (target == 0) {
            ans.push_back(path);
            return;
        }

        for (int i = index; i < candidates.size(); i++) {
            if (i > index && candidates[i] == candidates[i - 1]) {
                continue;
            }

            if (candidates[i] > target) {
                break;
            }

            path.push_back(candidates[i]);
            help(i + 1, target - candidates[i]);
            path.pop_back();
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target)
    {
        sort(candidates.begin(), candidates.end());
        this->candidates = candidates;

        help(0, target);
        return ans;
    }
};
// @lc code=end
