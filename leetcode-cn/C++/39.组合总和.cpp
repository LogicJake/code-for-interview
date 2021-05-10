/*
 * @lc app=leetcode.cn id=39 lang=cpp
 *
 * [39] 组合总和
 */

// @lc code=start
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> ans;

    void help(vector<int> candidates, int index, vector<int>& path, int target)
    {
        if (target == 0) {
            ans.emplace_back(path);
            return;
        }

        for (int i = index; i < candidates.size(); i++) {
            int num = candidates[i];
            if (num > target) {
                break;
            }
            path.push_back(num);
            help(candidates, i, path, target - num);
            path.pop_back();
        }
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target)
    {
        sort(candidates.begin(), candidates.end());

        vector<int> path;
        help(candidates, 0, path, target);

        return ans;
    }
};
// @lc code=end
