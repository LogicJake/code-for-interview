/*
 * @lc app=leetcode.cn id=909 lang=cpp
 *
 * [909] 蛇梯棋
 */

// @lc code=start
#include <queue>
#include <vector>
using namespace std;
class Solution {
public:
    pair<int, int> id2rc(int id, int n)
    {
        int r = (id - 1) / n, c = (id - 1) % n;
        if (r % 2 == 1) {
            c = n - 1 - c;
        }
        return { n - 1 - r, c };
    }

    int snakesAndLadders(vector<vector<int>>& board)
    {
        int n = board.size();
        queue<pair<int, int>> q;
        vector<int> vis(n * n + 1);

        q.emplace(1, 0);
        vis[1] = 1;

        while (!q.empty()) {
            auto cur = q.front();
            q.pop();

            for (int i = 1; i <= 6; i++) {
                int next_pos = cur.first + i;

                if (next_pos > n * n) {
                    break;
                }

                auto rc = id2rc(next_pos, n);
                if (board[rc.first][rc.second] > 0) {
                    next_pos = board[rc.first][rc.second];
                }

                if (next_pos == n * n) {
                    return cur.second + 1;
                }

                if (!vis[next_pos]) {
                    vis[next_pos] = 1;
                    q.emplace(next_pos, cur.second + 1);
                }
            }
        }
        return -1;
    }
};
// @lc code=end
