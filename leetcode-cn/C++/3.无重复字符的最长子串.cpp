/*
 * @lc app=leetcode.cn id=3 lang=cpp
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
#include <string>
#include <unordered_set>

using namespace std;

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_set<char> window;
        int left = 0;
        int right = 0;
        int ans = 0;

        while (right < s.size())
        {
            while (window.count(s[right]))
            {
                window.erase(s[left]);
                left += 1;
            }
            window.insert(s[right]);
            right += 1;

            ans = max(ans, right - left);
        }

        return ans;
    }
};

// @lc code=end
