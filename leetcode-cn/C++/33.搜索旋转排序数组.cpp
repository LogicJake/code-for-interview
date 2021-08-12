/*
 * @lc app=leetcode.cn id=33 lang=cpp
 *
 * [33] 搜索旋转排序数组
 */

// @lc code=start
#include <vector>
using namespace std;
class Solution {
public:
    int search(vector<int>& nums, int target)
    {
        int left = 0;
        int right = nums.size();
        int n = nums.size();

        while (left< right)
        {
            int mid = (left + right) / 2;

            if (nums[mid] == target)
            {
                return mid;
            }

            if (nums[mid] >= nums[0])
            {
                if (nums[0] <= target && nums[mid] > target)
                {
                    right = mid;
                }
                else
                {
                    left = mid + 1;
                }
            }
            else{
                if (nums[mid] < target && nums[n-1] >= target)
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid;
                } 
            }   
        }

        return -1;
        
    }
};
// @lc code=end
