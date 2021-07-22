#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target)
    {
        // 寻找出现target的第一个位置
        int left = 0;
        int right = nums.size();

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                right = mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid;
            }
        }

        int first = left;

        // 寻找出现target的最后一个位置

        left = 0;
        right = nums.size();

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                left = mid + 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid;
            }
        }

        int last = left - 1;

        return last - first + 1;
    }
};