/*
 * @lc app=leetcode.cn id=1744 lang=cpp
 *
 * [1744] 你能在你最喜欢的那天吃到你最喜欢的糖果吗？
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    vector<bool> canEat(vector<int>& candiesCount, vector<vector<int>>& queries)
    {
        vector<long long> sum_(candiesCount.size(), 0);
        for (int i = 1; i < candiesCount.size(); i++) {
            sum_[i] = sum_[i - 1] + candiesCount[i - 1];
        }

        vector<bool> ans(queries.size(), true);

        for (int i = 0; i < queries.size(); i++) {
            vector<int> query = queries[i];

            int type = query[0];
            int day = query[1];
            int cap = query[2];

            // 需求上下界
            long long down_bound = sum_[type] + 1;
            long long up_bound = sum_[type] + candiesCount[type];

            // 能力上下界
            long long down_bound_2 = (day + 1) * 1;
            long long up_bound_2 = (long long)(day + 1) * cap;

            if (up_bound_2 < down_bound || down_bound_2 > up_bound) {
                ans[i] = false;
            }
        }

        return ans;
    }
};
// @lc code=end
