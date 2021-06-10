#include <vector>
using namespace std;

class Solution {
public:
    vector<int> singleNumbers(vector<int>& nums)
    {
        int ret = 0;
        for (int num : nums) {
            ret ^= num;
        }

        int index = 1;
        while (ret & index == 0) {
            index <<= 1;
        }

        int a = 0;
        int b = 0;

        for (int num : nums) {
            if (num & index) {
                a ^= num;
            } else {
                b ^= num;
            }
        }
        return { a, b };
    }
};