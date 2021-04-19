/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 三数之和
 */

// @lc code=start
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums)
    {
        int n = nums.size();
        vector<vector<int>> ans;

        sort(nums.begin(), nums.end());
        for (int first = 0; first < (n - 2); first++) {
            if (first > 0 && nums[first] == nums[first - 1]) {
                continue;
            }

            if (nums[first] > 0) {
                break;
            }

            int second = first + 1;
            int third = nums.size() - 1;

            while (second < third) {
                if (second > first + 1 && nums[second] == nums[second - 1]) {
                    second++;
                    continue;
                }

                if (nums[first] + nums[second] + nums[third] == 0) {
                    ans.push_back({ nums[first], nums[second], nums[third] });
                    second++;
                    third--;

                } else if (nums[first] + nums[second] + nums[third] < 0) {
                    second++;
                } else if (nums[first] + nums[second] + nums[third] > 0) {
                    third--;
                }
            }
        }

        return ans;
    }
};
// @lc code=end
