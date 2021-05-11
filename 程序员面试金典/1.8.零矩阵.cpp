#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix)
    {
        int M = matrix.size();
        int N = matrix[0].size();

        unordered_set<int> hang;
        unordered_set<int> lie;

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (matrix[i][j] == 0) {
                    hang.insert(i);
                    lie.insert(j);
                }
            }
        }

        for (int i = 0; i < M; i++) {
            if (hang.count(i)) {
                for (int j = 0; j < N; j++) {
                    matrix[i][j] = 0;
                }
            } else {
                for (int j : lie) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
};