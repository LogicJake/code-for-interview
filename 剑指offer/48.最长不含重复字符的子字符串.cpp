#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_map<char, int> window;
        int left = 0;
        int right = 0;
        int ans = 0;
        while (right < s.size()) {
            char add_c = s[right];
            window[add_c] += 1;
            right += 1;

            while (window[add_c] == 2) {
                window[s[left]] -= 1;
                left += 1;
            }

            ans = max(ans, right - left);
        }

        return ans;
    }
};