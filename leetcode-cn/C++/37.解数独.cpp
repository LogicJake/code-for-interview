/*
 * @lc app=leetcode.cn id=37 lang=cpp
 *
 * [37] 解数独
 */

// @lc code=start
#include <string.h>
#include <vector>
using namespace std;

class Solution
{
public:
    bool hang[9][9];
    bool lie[9][9];
    bool block[9][9];
    vector<pair<int, int>> pos;
    bool ret = false;

    void help(int index, vector<vector<char>> &board)
    {
        if (index == pos.size())
        {
            ret = true;
            return;
        }

        auto [i, j] = pos[index];
        for (int num = 0; num < 9; num++)
        {
            if (!hang[i][num] && !lie[j][num] && !block[(i / 3) * 3 + j / 3][num])
            {
                if (ret)
                {
                    return;
                }

                board[i][j] = '1' + num;
                hang[i][num] = lie[j][num] = block[(i / 3) * 3 + j / 3][num] = true;
                help(index + 1, board);
                hang[i][num] = lie[j][num] = block[(i / 3) * 3 + j / 3][num] = false;
            }
        }
    }

    void solveSudoku(vector<vector<char>> &board)
    {
        memset(hang, false, sizeof(hang));
        memset(lie, false, sizeof(lie));
        memset(block, false, sizeof(block));

        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                if (board[i][j] == '.')
                {
                    pos.push_back({i, j});
                }
                else
                {
                    int num = board[i][j] - '1';
                    hang[i][num] = true;
                    lie[j][num] = true;
                    block[(i / 3) * 3 + j / 3][num] = true;
                }
            }
        }

        help(0, board);
    }
};
// @lc code=end
