/*
 * @lc app=leetcode.cn id=1074 lang=cpp
 *
 * [1074] 元素和为目标值的子矩阵数量
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k)
    {
        int n = nums.size();
        vector<int> mem(n + 1, 0);
        for (int i = 0; i < n; i++) {
            mem[i + 1] = mem[i] + nums[i];
        }

        unordered_map<int, int> map;
        int ans = 0;

        for (int i = 0; i < n + 1; i++) {
            if (map.find(mem[i] - k) != map.end()) {
                ans += map[mem[i] - k];
            }
            map[mem[i]]++;
        }

        return ans;
    }

    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target)
    {
        int ans = 0;
        int m = matrix.size();
        int n = matrix[0].size();

        // 循环上界
        for (int i = 0; i < m; i++) {
            vector<int> nums(n, 0);
            // 循环下界
            for (int j = i; j < m; j++) {
                for (int k = 0; k < n; k++) {
                    nums[k] += matrix[j][k];
                }
                ans += subarraySum(nums, target);
            }
        }

        return ans;
    }
};
// @lc code=end
