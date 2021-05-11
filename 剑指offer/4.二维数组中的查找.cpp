#include <vector>
using namespace std;

class Solution {
public:
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target)
    {
        int m = matrix.size();
        if (m == 0) {
            return false;
        }

        int n = matrix[0].size();
        if (n == 0) {
            return false;
        }

        int hang = m - 1;
        int lie = 0;

        while (hang >= 0 && lie < n) {
            if (matrix[hang][lie] == target) {
                return true;
            } else if (matrix[hang][lie] > target) {
                hang -= 1;
            } else if (matrix[hang][lie] < target) {
                lie += 1;
            }
        }
        return false;
    }
};