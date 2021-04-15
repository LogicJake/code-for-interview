/*
 * @lc app=leetcode.cn id=5 lang=cpp
 *
 * [5] 最长回文子串
 */

// @lc code=start
#include <string>
using namespace std;

class Solution {
public:
    pair<int, int> help(const string s, int left, int right)
    {
        while (left >= 0 && right < s.size() && s[left] == s[right]) {
            left -= 1;
            right += 1;
        }
        left++;
        right--;
        return { left, right };
    }

    string longestPalindrome(string s)
    {
        int start = 0;
        int end = 0;

        for (int i = 0; i < s.size(); i++) {
            auto [left1, right1] = help(s, i, i);
            auto [left2, right2] = help(s, i, i + 1);

            if (right1 - left1 > end - start) {
                start = left1;
                end = right1;
            }

            if (right2 - left2 > end - start) {
                start = left2;
                end = right2;
            }
        }
        return s.substr(start, end - start + 1);
    }
};
// @lc code=end
