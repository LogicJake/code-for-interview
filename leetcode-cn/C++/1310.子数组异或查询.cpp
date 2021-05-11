/*
 * @lc app=leetcode.cn id=1310 lang=cpp
 *
 * [1310] 子数组异或查询
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries)
    {
        vector<int> result;
        result.push_back(0);
        for (int i = 0; i < arr.size(); i++) {
            result.push_back(result.back() ^ arr[i]);
        }

        vector<int> ans;
        for (vector<int> query : queries) {
            int left = query[0] + 1;
            int right = query[1] + 1;

            ans.push_back(result[right] ^ result[left - 1]);
        }

        return ans;
    }
};
// @lc code=end
