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

class Solution
{
public:
    vector<int> findSubstring(string s, vector<string> &words)
    {
        vector<int> ans;
        int d = words[0].size();
        int size = s.size();
        int n = words.size();

        unordered_map<string, int> mem;
        for (string word : words)
        {
            mem[word] += 1;
        }

        vector<unordered_map<string, int>> window(d);

        // 初始化
        for (int i = 0; i < d && i + n * d <= size; i++)
        {
            for (int j = i; j < n * d; j += d)
            {
                string str = s.substr(j, d);
                window[i][str] += 1;
            }

            if (window[i] == mem)
            {
                ans.push_back(i);
            }
        }

        for (int i = d; i < size && i + n * d <= size; i++)
        {
            int index = i % d;
            string add_str = s.substr(i + n * d - d, d);
            string remove_str = s.substr(i - d, d);

            window[index][remove_str] -= 1;
            if (window[index][remove_str] == 0)
            {
                window[index].erase(remove_str);
            }
            window[index][add_str] += 1;

            if (window[index] == mem)
            {
                ans.push_back(i);
            }
        }
        return ans;
    }
};
// @lc code=end
