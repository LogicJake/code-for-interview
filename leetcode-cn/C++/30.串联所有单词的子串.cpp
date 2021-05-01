/*
 * @lc app=leetcode.cn id=30 lang=cpp
 *
 * [30] 串联所有单词的子串
 */

// @lc code=start
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words)
    {
        vector<int> ans;

        int n = s.size(), m = words.size(), d = words[0].size();
        int len = 0;

        unordered_map<string, int> words_mp;
        for (string s : words) {
            len += d;
            words_mp[s] += 1;
        }

        vector<unordered_map<string, int>> window(d);
        // 遍历每一个窗口的初始
        for (int i = 0; i < d && i + len <= n; i++) {
            for (int j = i; j < i + len; j += d) {
                string tmp = s.substr(j, d);
                window[i][tmp]++;
            }
            if (window[i] == words_mp) {
                ans.push_back(i);
            }
        }

        for (int i = d; i + len <= n; i++) {
            int index = i % d;

            string rs = s.substr(i - d, d);
            string as = s.substr(i - d + len, d);

            // 这样写就对
            if (--window[index][rs] == 0) {
                window[index].erase(rs);
            }

            window[index][as] += 1;

            if (window[index] == words_mp) {
                ans.push_back(i);
            }
        }

        return ans;
    }
};
// @lc code=end
