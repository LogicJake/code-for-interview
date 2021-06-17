#include <vector>
using namespace std;

class Solution {
public:
    vector<int> exchange(vector<int>& nums)
    {

        if (nums.size() == 0) {
            return nums;
        }

        int left = 0;
        int right = nums.size() - 1;

        int privot = nums[left];

        while (left < right) {
            while (left < right && nums[right] % 2 == 0) {
                right -= 1;
            }
            nums[left] = nums[right];

            while (left < right && nums[left] % 2 == 1) {
                left += 1;
            }
            nums[right] = nums[left];
        }
        nums[left] = privot;

        return nums;
    }
};