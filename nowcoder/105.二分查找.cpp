#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 如果目标值存在返回下标，否则返回 -1
     * @param nums int整型vector 
     * @param target int整型 
     * @return int整型
     */
    int search(vector<int>& nums, int target)
    {
        int i = 0;
        int j = nums.size();

        if (j == 0) {
            return -1;
        }

        while (i < j) {
            int mid = (i + j) / 2;

            if (nums[mid] == target) {
                j = mid;
            } else if (nums[mid] > target) {
                j = mid;
            } else if (nums[mid] < target) {
                i = mid + 1;
            }
        }

        if (nums[j] == target) {
            return j;
        } else {
            return -1;
        }
    }
};