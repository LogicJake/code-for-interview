#include <vector>
using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix)
    {
        int N = matrix.size();

        for (int i = 0; i < N; i++) {
            for (int j = i; j < N; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }

        for (int i = 0; i < N; i++) {
            int left = 0;
            int right = N - 1;

            while (left <= right) {
                swap(matrix[i][left], matrix[i][right]);

                left += 1;
                right -= 1;
            }
        }
    }
};