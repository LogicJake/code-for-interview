#include <string>
#include <vector>

using namespace std;
class Solution {
public:
    int getLongestPalindrome(string A, int n)
    {
        vector<vector<int>> dp(n, vector<int>(n));
        int ans = 0;

        for (int i = 0; i < n; i++) {
            int left = i;
            int right = i;
            while (left >= 0 && right < n && A[right] == A[left]) {
                left--;
                right++;
            }
            ans = max(ans, right - left - 1);

            left = i;
            right = i + 1;
            while (left >= 0 && right < n && A[right] == A[left]) {
                left--;
                right++;
            }
            ans = max(ans, right - left - 1);
        }

        return ans;
    }
};