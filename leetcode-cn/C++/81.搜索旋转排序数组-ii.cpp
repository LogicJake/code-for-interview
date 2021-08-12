/*
 * @lc app=leetcode.cn id=81 lang=cpp
 *
 * [81] 搜索旋转排序数组 II
 */

// @lc code=start
#include<vector>
using namespace std;


class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right)
        {
            int mid = (left + right) / 2;
            if (nums[mid] == target)
            {
                return true;
            }

            if (nums[mid] == nums[left] && nums[mid] == nums[right])
            {
                left += 1;
                right -= 1;
            }
            else if (nums[mid] >= nums[left])
            {
                if (nums[left] <= target && target < nums[mid])
                {
                    right = mid - 1;
                }
                else{
                    left = mid + 1;
                } 
            }
            else
            {
                if (nums[mid] < target && target <= nums[right])
                {
                    left = mid + 1;
                }
                else{
                    right = mid - 1;
                } 
            }
        }
        
        return false;
    }
};
// @lc code=end

