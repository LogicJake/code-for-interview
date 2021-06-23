#include <vector>
using namespace std;
class Solution {
public:
    int mergeSort(vector<int>& nums, vector<int>& tmp, int left, int right)
    {
        if (left >= right) {
            return 0;
        }

        int mid = left + (right - left) / 2;
        int leftNum = mergeSort(nums, tmp, left, mid);
        int rightNum = mergeSort(nums, tmp, mid + 1, right);

        int pos = left;
        int l = left;
        int r = mid + 1;
        int crossNum = 0;

        while (l <= mid && r <= right) {
            if (nums[r] < nums[l]) {
                crossNum += (mid - l + 1);
                tmp[pos] = nums[r];
                r++;
            } else {
                tmp[pos] = nums[l];
                l++;
            }
            pos++;
        }

        while (l <= mid) {
            tmp[pos] = nums[l];
            l++;
            pos++;
        }

        while (r <= right) {
            crossNum += (mid - l + 1);
            tmp[pos] = nums[r];
            r++;
            pos++;
        }
        copy(tmp.begin() + left, tmp.begin() + right + 1, nums.begin() + left);

        return leftNum + rightNum + crossNum;
    }

    int reversePairs(vector<int>& nums)
    {
        int n = nums.size();
        vector<int> tmp(n);
        return mergeSort(nums, tmp, 0, n - 1);
    }
};