/*
 * @lc app=leetcode.cn id=3 lang=cpp
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s)
    {
        int ans = 0;
        int left = 0;
        int right = 0;
        unordered_set<int> window;

        while (right < s.size()) {
            char c = s[right];

            right += 1;

            while (window.count(c)) {
                window.erase(s[left]);
                left += 1;
            }

            window.insert(c);
            ans = max(ans, right - left);
        }

        return ans;
    }
};
// @lc code=end
