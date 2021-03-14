#include <vector>
using namespace std;

class Solution {
public:
    /**
   * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
   * 将给定数组排序
   * @param arr int整型vector 待排序的数组
   * @return int整型vector
   */
    vector<int> MySort(vector<int>& arr)
    {
        QuickSort(arr, 0, arr.size() - 1);
        return arr;
    }

    void QuickSort(vector<int>& nums, int left, int right)
    {
        if (left >= right) {
            return;
        }

        int privot = nums[left];
        int i = left;
        int j = right;

        while (i < j) {
            while (i < j && nums[j] >= privot) {
                j -= 1;
            }
            nums[i] = nums[j];

            while (i < j && nums[i] <= privot) {
                i += 1;
            }
            nums[j] = nums[i];
        }
        nums[i] = privot;
        QuickSort(nums, left, i - 1);
        QuickSort(nums, i + 1, right);
    }
};