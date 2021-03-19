#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    /**
     * max sum of the subarray
     * @param arr int整型vector the array
     * @return int整型
     */
    int maxsumofSubarray(vector<int>& arr)
    {
        int ans = -999999;
        int max_ = -999999;
        for (int num : arr) {
            max_ = max(max_ + num, num);
            ans = max(ans, max_);
        }

        return ans;
    }
};