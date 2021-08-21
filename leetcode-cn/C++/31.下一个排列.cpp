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

        if (n <= 1)
        {
            return;
        }

        int i = n - 2;
        for (; i >= 0; i--)
        {
            if (nums[i] < nums[i + 1])
            {

                break;
            }
        }

        if (i >= 0)
        {
            for (int j = n - 1; j >= i + 1; j--)
            {
                if (nums[j] > nums[i])
                {
                    int temp = nums[j];
                    nums[j] = nums[i];
                    nums[i] = temp;
                    break;
                }
            }
        }

        sort(nums.begin() + i + 1, nums.end());
    }
};

// @lc code=end
