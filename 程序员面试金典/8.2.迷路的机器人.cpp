#include <vector>
using namespace std;

class Solution {
public:
    int m = 0;
    int n = 0;
    bool find = false;

    vector<vector<int>> path;
    vector<vector<int>> visited;
    vector<vector<int>> obstacleGrid;

    void help(int x, int y)
    {
        if (x >= m || y >= n || obstacleGrid[x][y] == 1 || visited[x][y] == 1) {
            return;
        }

        path.push_back({ x, y });
        visited[x][y] = 1;

        if (x == m - 1 && y == n - 1) {
            find = true;
            return;
        }

        help(x, y + 1);
        if (find)
            return;

        help(x + 1, y);

        if (find)
            return;

        path.pop_back();
    }

    vector<vector<int>> pathWithObstacles(vector<vector<int>>& obstacleGrid)
    {
        int m = obstacleGrid.size();

        if (m == 0) {
            return path;
        }

        int n = obstacleGrid[0].size();

        if (obstacleGrid[m - 1][n - 1] == 1) {
            return path;
        }

        this->m = m;
        this->n = n;

        vector<vector<int>> visited(m, vector<int>(n, 0));

        this->visited = visited;
        this->obstacleGrid = obstacleGrid;

        help(0, 0);

        return path;
    }
};