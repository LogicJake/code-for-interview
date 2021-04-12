/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */

// @lc code=start
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        int left = 0;
        int right = nums.size() - 1;

        unordered_map<int, int> mem;

        int i = 0;
        for (; i < nums.size(); i++) {
            if (mem.find(target - nums[i]) != mem.end()) {
                return { mem[target - nums[i]], i };
            } else {
                mem[nums[i]] = i;
            }
        }
        return {};
    }
};
// @lc code=end
