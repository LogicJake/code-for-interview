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

class Solution
{
public:
    vector<vector<int>> fourSum(vector<int> &nums, int target)
    {
        sort(nums.begin(), nums.end());
        int n = nums.size();

        vector<vector<int>> ans;
        long long sum_ = 0;
        for (int first = 0; first < n - 3; first++)
        {
            if (first > 0 && nums[first] == nums[first - 1])
            {
                continue;
            }

            sum_ = nums[first] + nums[first + 1] + nums[first + 2] + nums[first + 3];
            if (sum_ > target)
            {
                break;
            }

            for (int second = first + 1; second < n; second++)
            {
                if (second > first + 1 && nums[second - 1] == nums[second])
                {
                    continue;
                }

                int third = second + 1;
                int forth = n - 1;

                while (third < forth)
                {
                    long long sum_ = 0;
                    for (int i : {first, second, third, forth})
                    {
                        sum_ += nums[i];
                    }

                    if (sum_ < target)
                    {
                        third++;
                    }
                    else if (sum_ > target)
                    {
                        forth--;
                    }
                    else
                    {
                        ans.push_back({nums[first], nums[second], nums[third], nums[forth]});

                        while (third < forth && nums[third] == nums[third + 1])
                        {
                            third++;
                        }
                        third++;

                        while (third < forth && nums[forth] == nums[forth - 1])
                        {
                            forth--;
                        }
                        forth--;
                    }
                }
            }
        }

        return ans;
    }
};
// @lc code=end
