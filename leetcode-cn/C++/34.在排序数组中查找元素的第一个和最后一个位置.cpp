/*
 * @lc app=leetcode.cn id=34 lang=cpp
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    int firstSearch(vector<int>& nums, int target)
    {
        int left = 0;
        int right = nums.size() - 1;

        while (left < right) {
            int mid = (left + right) / 2;

            if (nums[mid] == target) {
                right = mid;
            } else if (nums[mid] > target) {
                right = mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            }
        }

        if (left < nums.size() && nums[left] == target) {
            return left;
        } else {
            return -1;
        }
    }

    int lastSearch(vector<int>& nums, int target)
    {
        int left = 0;
        int right = nums.size() - 1;

        while (left < right) {
            int mid = (left + right) / 2;

            if (nums[mid] == target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            }
        }

        if (nums[left] == target) {
            return left;
        } else if (left - 1 >= 0 && nums[left - 1] == target) {
            return left - 1;
        } else {
            return -1;
        }
    }

    vector<int> searchRange(vector<int>& nums, int target)
    {
        int first = firstSearch(nums, target);
        if (first == -1) {
            return { -1, -1 };
        }

        int last = lastSearch(nums, target);
        return { first, last };
    }
};
// @lc code=end
