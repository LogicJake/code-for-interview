/*
 * @lc app=leetcode.cn id=692 lang=cpp
 *
 * [692] 前K个高频单词
 */

// @lc code=start
#include <algorithm>
#include <queue>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    using PIS = pair<int, string>;

    struct cmp {
        bool operator()(const PIS& p1, const PIS& p2)
        {
            if (p1.first == p2.first)
                return p1.second < p2.second;
            return p1.first > p2.first;
        }
    };

    vector<string> topKFrequent(vector<string>& words, int k)
    {
        unordered_map<string, int> cnt;

        for (string word : words) {
            cnt[word] += 1;
        }

        priority_queue<PIS, vector<PIS>, cmp> pq;
        for (auto& [key, value] : cnt) {
            pq.push({ value, key });
            if (pq.size() > k) {
                pq.pop();
            }
        }

        vector<string> ans;

        while (!pq.empty()) {
            auto v = pq.top().second;
            ans.push_back(v);
            pq.pop();
        }

        reverse(ans.begin(), ans.end());

        return ans;
    }
};
// @lc code=end
