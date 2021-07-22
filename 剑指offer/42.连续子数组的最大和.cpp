#include <vector>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums)
    {
        int pre = -9999;
        int ans = pre;

        for (int num : nums) {
            int cur = max(num, pre + num);
            pre = cur;
            ans = max(ans, pre);
        }

        return ans;
    }
};