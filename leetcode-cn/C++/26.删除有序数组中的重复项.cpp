/*
 * @lc app=leetcode.cn id=26 lang=cpp
 *
 * [26] 删除排序数组中的重复项
 */

// @lc code=start
#include <vector>
using namespace std;
class Solution {
public:
    int removeDuplicates(vector<int>& nums)
    {
        if (nums.size() == 0) {
            return 0;
        }

        int i = 1;
        int j = 1;

        while (j < nums.size()) {
            if (nums[j] != nums[i - 1]) {
                nums[i] = nums[j];
                i++;
            }
            j++;
        }
        return i;
    }
};
// @lc code=end
