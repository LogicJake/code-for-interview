#include <vector>
using namespace std;

class Solution {
public:
    int ans = 0;
    int m = 0;
    int n = 0;
    int k = 0;

    int numSum(int num)
    {
        int sum_ = 0;
        while (num > 0) {
            sum_ += num % 10;
            num = num / 10;
        }
        return sum_;
    }

    void dfs(int x, int y, vector<vector<int>>& visited)
    {
        if (x < 0 || x >= m || y < 0 || y >= n || numSum(x) + numSum(y) > k || visited[x][y] == 1) {
            return;
        }

        ans += 1;
        visited[x][y] = 1;

        dfs(x, y + 1, visited);
        dfs(x, y - 1, visited);
        dfs(x + 1, y, visited);
        dfs(x - 1, y, visited);
    }

    int movingCount(int m_, int n_, int k_)
    {
        m = m_;
        n = n_;
        k = k_;
        vector<vector<int>> visited(m, vector<int>(n, 0));

        dfs(0, 0, visited);
        return ans;
    }
};