/*
 * @lc app=leetcode.cn id=815 lang=cpp
 *
 * [815] 公交路线
 */

// @lc code=start
#include <queue>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target)
    {
        if (source == target) {
            return 0;
        }

        int n = routes.size();

        vector<vector<int>> edge(n, vector<int>(n));
        unordered_map<int, vector<int>> rec;

        for (int bus1 = 0; bus1 < n; bus1++) {
            for (int site : routes[bus1]) {
                for (int bus2 : rec[site]) {
                    edge[bus2][bus1] = edge[bus1][bus2] = true;
                }
                rec[site].push_back(bus1);
            }
        }

        queue<pair<int, int>> q;
        vector<bool> vis(n, false);
        for (int bus : rec[source]) {
            if (find(rec[target].begin(), rec[target].end(), bus) != rec[target].end()) {
                return 1;
            }

            q.emplace(bus, 1);
            vis[bus] = 1;
        }

        int ans = INT32_MAX;

        while (!q.empty()) {
            auto [bus, num] = q.front();
            q.pop();

            for (int next_bus = 0; next_bus < n; next_bus++) {
                if (!edge[bus][next_bus] || vis[next_bus]) {
                    continue;
                }

                if (find(rec[target].begin(), rec[target].end(), next_bus) != rec[target].end()) {
                    ans = min(ans, num + 1);
                } else {
                    q.emplace(next_bus, num + 1);
                    vis[next_bus] = 1;
                }
            }
        }

        if (ans == INT32_MAX) {
            return -1;
        }
        return ans;
    }
};
// @lc code=end
