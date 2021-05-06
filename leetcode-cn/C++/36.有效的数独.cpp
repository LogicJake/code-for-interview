/*
 * @lc app=leetcode.cn id=36 lang=cpp
 *
 * [36] 有效的数独
 */

// @lc code=start
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board)
    {
        vector<vector<bool>> hang(9, vector<bool>(9, false));
        vector<vector<bool>> lie(9, vector<bool>(9, false));
        vector<vector<bool>> jiu(9, vector<bool>(9, false));

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    continue;
                }
                int num = board[i][j] - '1';

                if (hang[i][num]) {
                    return false;
                }

                if (lie[j][num]) {
                    return false;
                }

                if (jiu[i / 3 * 3 + j / 3][num]) {
                    return false;
                }

                hang[i][num] = true;
                lie[j][num] = true;
                jiu[i / 3 * 3 + j / 3][num] = true;
            }
        }
        return true;
    }
};
// @lc code=end
