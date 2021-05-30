/*
 * @lc app=leetcode.cn id=5754 lang=cpp
 *
 * [5754] 长度为三且各字符不同的子字符串
 */

// @lc code=start
#include <algorithm>
#include <iostream>
#include <set>
#include <string>

using namespace std;

class Solution {
public:
    int check(vector<int>& alpha)
    {
        for (int i = 0; i < 26; i++)
            if (alpha[i] > 1)
                return 0;
        return 1;
    }
    int countGoodSubstrings(string s)
    {
        int ans = 0;
        int n = s.size();
        vector<int> alpha(26, 0);
        for (int i = 0; i < n; i++) {
            alpha[s[i] - 'a']++;
            if (i >= 3)
                alpha[s[i - 3] - 'a']--;
            if (i >= 2)
                ans += check(alpha);
        }
        return ans;
    }
};
// @lc code=end
