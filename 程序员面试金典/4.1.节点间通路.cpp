#include <vector>
using namespace std;

class Solution {
public:
    bool find = false;
    vector<vector<int>> map;
    vector<bool> visited;
    int target = 0;

    void dfs(int cur)
    {
        if (cur == target) {
            find = true;
        }

        visited[cur] = true;

        for (auto x : map[cur]) {
            if (visited[x]) {
                continue;
            }

            dfs(x);
            if (find) {
                break;
            }
        }
    }

    bool findWhetherExistsPath(int n, vector<vector<int>>& graph, int start, int target)
    {
        map = vector<vector<int>>(n);
        visited = vector<bool>(n, false);

        for (int i = 0; i < graph.size(); i++) {
            int start = graph[i][0];
            int end = graph[i][1];
            map[start].push_back(end);
        }
        this->target = target;
        dfs(start);

        return find;
    }
};