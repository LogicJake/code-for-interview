/*
 * @lc app=leetcode.cn id=1738 lang=cpp
 *
 * [1738] 找出第 K 大的异或坐标值
 */

// @lc code=start
#include <algorithm>
#include <functional>
#include <vector>

using namespace std;

class Solution {
public:
    int kthLargestValue(vector<vector<int>>& matrix, int k)
    {
        int m = matrix.size();
        int n = matrix[0].size();

        vector<vector<int>> pre(m + 1, vector<int>(n + 1, 0));
        vector<int> nums;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                pre[i][j] = pre[i - 1][j] ^ pre[i][j - 1] ^ pre[i - 1][j - 1] ^ matrix[i - 1][j - 1];
                nums.push_back(pre[i][j]);
            }
        }
        sort(nums.begin(), nums.end(), greater<int>());
        return nums[k - 1];
    }
};
// @lc code=end
