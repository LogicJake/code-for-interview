/*
 * @lc app=leetcode.cn id=1720 lang=cpp
 *
 * [1720] 解码异或后的数组
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first)
    {
        vector<int> ans;
        ans.push_back(first);

        for (int num : encoded) {
            int decoded = num ^ first;
            ans.push_back(decoded);
            first = decoded;
        }

        return ans;
    }
};
// @lc code=end
