#include <algorithm>
#include <set>
#include <vector>
using namespace std;

class Solution {
public:
    /**
     * 
     * @param arr int整型vector the array
     * @return int整型
     */
    int maxLength(vector<int>& arr)
    {
        int left = 0;
        int right = 0;

        set<int> window;
        int ans = 0;

        while (right < arr.size()) {
            int num = arr[right];
            right += 1;

            // 已经有过了
            if (window.find(num) != window.end()) {
                while (left < right && arr[left] != num) {
                    window.erase(window.find(arr[left]));
                    left += 1;
                }
                left += 1;
            } else {
                window.insert(num);
            }
            ans = max(ans, right - left);
        }
        return ans;
    }
};