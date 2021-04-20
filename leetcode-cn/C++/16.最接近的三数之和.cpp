/*
 * @lc app=leetcode.cn id=16 lang=cpp
 *
 * [16] 最接近的三数之和
 */

// @lc code=start
#include <algorithm>
#include <limits.h>
#include <vector>

using namespace std;
class Solution {
public:
    int ans = 1e7;

    int threeSumClosest(vector<int>& nums, int target)
    {
        int n = nums.size();

        sort(nums.begin(), nums.end());
        for (int first = 0; first < (n - 2); first++) {
            if (first > 0 && nums[first] == nums[first - 1]) {
                continue;
            }

            int second = first + 1;
            int third = nums.size() - 1;

            while (second < third) {
                if (second > first + 1 && nums[second] == nums[second - 1]) {
                    second++;
                    continue;
                }

                int num = nums[first] + nums[second] + nums[third];

                if (abs(num - target) < abs(ans - target)) {
                    ans = num;
                }

                if (num == target) {
                    return num;
                } else if (num < target) {
                    second++;
                } else if (num > target) {
                    third--;
                }
            }
        }
        return ans;
    }
};
// @lc code=end
