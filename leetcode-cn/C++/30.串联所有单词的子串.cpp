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
        int d = words[0].size();
        int n = s.size();
        int m = words.size();
        int len = m * d;
        unordered_map<string, int> mp;

        for (string word : words) {
            mp[word]++;
        }

        vector<unordered_map<string, int>> window(d);
        for (int i = 0; i + len <= n && i < d; i++) {
            for (int j = i; j < i + len; j += d) {
                string substr = s.substr(j, d);
                window[i][substr]++;
            }

            if (window[i] == mp) {
                ans.push_back(i);
            }
        }

        for (int i = d; i + len <= n; i++) {
            int index = i % d;

            string remove_str = s.substr(i - d, d);
            string add_str = s.substr(i + len - d, d);

            window[index][remove_str]--;
            if (window[index][remove_str] == 0) {
                window[index].erase(remove_str);
            }
            window[index][add_str]++;

            if (window[index] == mp) {
                ans.push_back(i);
            }
        }

        return ans;
    }
};
// @lc code=end
