#include <vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums)
    {
        vector<int> bit(32, 0);

        for (int num : nums) {
            for (int i = 0; i < 32; i++) {
                bit[i] += num & 1;
                num >>= 1;
            }
        }

        int ans = 0;

        for (int i = 31; i >= 0; i--) {
            ans <<= 1;
            ans += bit[i] % 3;
        }

        return ans;
    }
};