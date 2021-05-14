/*
 * @lc app=leetcode.cn id=18 lang=cpp
 *
 * [18] 四数之和
 */

// @lc code=start
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target)
    {
        int n = nums.size();
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        for (int first = 0; first < n - 3; first++) {
            if (first > 0 && nums[first] == nums[first - 1]) {
                continue;
            }

            if (nums[first] + nums[first + 1] + nums[first + 2] + nums[first + 3] > target) {
                break;
            }

            if (nums[first] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target) {
                continue;
            }

            for (int second = first + 1; second < n - 2; second++) {
                if (second > first + 1 && nums[second] == nums[second - 1]) {
                    continue;
                }

                if (nums[first] + nums[second] + nums[second + 1] + nums[second + 2] > target) {
                    break;
                }

                if (nums[first] + nums[second] + nums[n - 1] + nums[n - 2] < target) {
                    continue;
                }

                int third = second + 1;
                int forth = n - 1;

                while (third < forth) {
                    if (third > second + 1 && nums[third] == nums[third - 1]) {
                        third++;
                        continue;
                    }

                    if (nums[first] + nums[second] + nums[third] + nums[forth] < target) {
                        third++;
                    } else if (nums[first] + nums[second] + nums[third] + nums[forth] > target) {
                        forth--;
                    } else {
                        ans.push_back({ nums[first], nums[second], nums[third], nums[forth] });
                        third++;
                        forth--;
                    }
                }
            }
        }

        return ans;
    }
};
// @lc code=end
