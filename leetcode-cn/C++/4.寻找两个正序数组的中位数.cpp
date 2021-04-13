/*
 * @lc app=leetcode.cn id=4 lang=cpp
 *
 * [4] 寻找两个正序数组的中位数
 */

// @lc code=start
#include <vector>

using namespace std;

class Solution {
public:
    int getKthElement(const vector<int>& nums1, const vector<int>& nums2, int k)
    {
        int index1 = 0;
        int index2 = 0;

        int m = nums1.size();
        int n = nums2.size();

        while (true) {
            if (index1 == m) {
                return nums2[index2 + k - 1];
            }
            if (index2 == n) {
                return nums1[index1 + k - 1];
            }
            // 不能先判断 k == 1，因为 index1 和 index2 可能已经越界
            if (k == 1) {
                return min(nums1[index1], nums2[index2]);
            }

            int new_index1 = min(index1 + k / 2 - 1, m - 1);
            int new_index2 = min(index2 + k / 2 - 1, n - 1);

            int pivot1 = nums1[new_index1];
            int pivot2 = nums2[new_index2];

            if (pivot1 <= pivot2) {
                k = k - (new_index1 - index1 + 1);
                index1 = new_index1 + 1;
            } else {
                k = k - (new_index2 - index2 + 1);
                index2 = new_index2 + 1;
            }
        }
    }

    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2)
    {
        int total = nums1.size() + nums2.size();

        if (total % 2 == 1) {
            return getKthElement(nums1, nums2, (total + 1) / 2);
        } else {
            return (getKthElement(nums1, nums2, total / 2) + getKthElement(nums1, nums2, total / 2 + 1)) / 2.0;
        }
    }
};
// @lc code=end
