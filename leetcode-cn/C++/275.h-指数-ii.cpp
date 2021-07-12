/*
 * @lc app=leetcode.cn id=275 lang=cpp
 *
 * [275] H 指数 II
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution
{
public:
    int hIndex(vector<int> &citations)
    {
        int n = citations.size();

        int left = 0;
        int right = n;

        while (left < right)
        {
            int mid = left + (right - left) / 2;

            if (citations[mid] >= n - mid)
            {
                right = mid;
            }
            else
            {
                left = mid + 1;
            }
        }

        return n - left;
    }
};
// @lc code=end
