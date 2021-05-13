#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int m = 0;
    int n = 0;

    bool dfs(vector<vector<char>> board, const string word, int i, int j, int k)
    {
        if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != word[k]) {
            return false;
        }

        if (k == word.size() - 1) {
            return true;
        }

        board[i][j] = '\0';

        bool res = dfs(board, word, i, j + 1, k + 1) || dfs(board, word, i, j - 1, k + 1) || dfs(board, word, i + 1, j, k + 1) || dfs(board, word, i - 1, j, k + 1);

        board[i][j] = word[k];

        return res;
    }

    bool exist(vector<vector<char>>& board, string word)
    {
        m = board.size();
        n = board[0].size();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
};