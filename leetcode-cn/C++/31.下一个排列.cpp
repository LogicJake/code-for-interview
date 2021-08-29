/*
 * @lc app=leetcode.cn id=31 lang=cpp
 *
 * [31] 下一个排列
 */

// @lc code=start
#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
public:
    void nextPermutation(vector<int> &nums)
    {
        int n = nums.size();
        if (n == 1)
        {
            return;
        }

        int i = n - 2;

        while (i >= 0)
        {
            if (nums[i] < nums[i + 1])
            {
                break;
            }
            i--;
        }

        if (i < 0)
        {
            sort(nums.begin(), nums.end());
            return;
        }

        int j = n - 1;
        while (nums[j] <= nums[i])
        {
            j--;
        }

        int temp = nums[j];
        nums[j] = nums[i];
        nums[i] = temp;

        sort(nums.begin() + i + 1, nums.end());
    }
};

// @lc code=end
