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
        unordered_set<char> mem;
        int left = 0;
        int right = 0;
        int ans = 0;

        while (right < s.size()) {
            char c = s[right];
            right++;

            while (mem.count(c) != 0) {
                mem.erase(s[left]);
                left++;
            }
            mem.insert(c);

            ans = max(ans, right - left);
        }
        return ans;
    }
};
// @lc code=end
