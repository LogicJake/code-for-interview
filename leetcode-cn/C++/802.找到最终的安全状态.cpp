/*
 * @lc app=leetcode.cn id=802 lang=cpp
 *
 * [802] 找到最终的安全状态
 */

// @lc code=start
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph)
    {
        int n = graph.size();
        vector<vector<int>> path(n);
        vector<int> indegree(n, 0);

        for (int i = 0; i < n; i++) {
            for (int j : graph[i]) {
                path[j].push_back(i);
            }
            indegree[i] = graph[i].size();
        }

        vector<int> ans;
        queue<int> q;

        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            int i = q.front();
            ans.push_back(i);
            q.pop();

            for (int j : path[i]) {
                indegree[j] -= 1;
                if (indegree[j] == 0) {
                    q.push(j);
                }
            }
        }

        sort(ans.begin(), ans.end());
        return ans;
    }
};
// @lc code=end
