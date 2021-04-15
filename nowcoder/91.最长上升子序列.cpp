#include <vector>
using namespace std;
#define INT_MAX 2147483647

class Solution {
public:
    /**
     * retrun the longest increasing subsequence
     * @param arr int整型vector the array
     * @return int整型vector
     */
    vector<int> LIS(vector<int>& arr)
    {
        // write code here
        if (arr.size() <= 1)
            return arr;
        vector<int> dp(arr.size(), 0);
        vector<int> pos(arr.size(), 0); //pos[i]=j用来记录nums[i]在dp中的第j个位置
        int len = 0;
        dp[len] = arr[0];
        for (int i = 1; i < arr.size(); ++i) {
            if (arr[i] > dp[len]) {
                dp[++len] = arr[i];
                pos[i] = len;
            } else {
                int low = 0, high = len;
                while (low <= high) {
                    int mid = (low + high) >> 1;
                    if (dp[mid] < arr[i])
                        low = mid + 1;
                    else
                        high = mid - 1;
                }
                if (low != -1) {
                    dp[low] = arr[i];
                    pos[i] = low;
                } else {
                    dp[0] = arr[i];
                    pos[i] = 0;
                }
            }
        }
        vector<int> res(len + 1, INT_MAX);
        for (int i = arr.size() - 1; i >= 0; i--) {
            if (pos[i] == len) {
                res[len] = min(res[len], arr[i]);
                len--;
            }
        }
        return res;
    }
};