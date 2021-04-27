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
        vector<vector<int>> ans;
        if (nums.size() < 4) {
            return ans;
        }
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size() - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            if (nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target) {
                break;
            }
            if (nums[i] + nums[nums.size() - 3] + nums[nums.size() - 2] + nums[nums.size() - 1] < target) {
                continue;
            }

            for (int j = i + 1; j < nums.size() - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }

                if (nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target) {
                    break;
                }

                if (nums[i] + nums[j] + nums[nums.size() - 2] + nums[nums.size() - 1] < target) {
                    continue;
                }

                int left = j + 1;
                int right = nums.size() - 1;

                while (left < right) {
                    if (left > j + 1 && nums[left] == nums[left - 1]) {
                        left += 1;
                        continue;
                    }

                    int sum = nums[i] + nums[j] + nums[left] + nums[right];

                    if (sum < target) {
                        left += 1;
                    } else if (sum > target) {
                        right -= 1;
                    } else {
                        ans.push_back({ nums[i], nums[j], nums[left], nums[right] });
                        left += 1;
                        right -= 1;
                    }
                }
            }
        }

        return ans;
    }
};
// @lc code=end
