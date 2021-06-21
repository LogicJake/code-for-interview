#include <vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix)
    {
        int m = matrix.size();
        if (m == 0) {
            return {};
        }
        int n = matrix[0].size();

        int left = 0;
        int right = n;

        int top = 0;
        int button = m;

        vector<int> ans;
        while (left < right && top < button) {
            for (int i = left; i < right; i++) {
                ans.push_back(matrix[top][i]);
            }
            top++;

            for (int i = top; i < button; i++) {
                ans.push_back(matrix[i][right - 1]);
            }
            right--;

            if (left < right && top < button) {

                for (int i = right - 1; i >= left; i--) {
                    ans.push_back(matrix[button - 1][i]);
                }
                button--;

                for (int i = button - 1; i >= top; i--) {
                    ans.push_back(matrix[i][left]);
                }
                left++;
            }
        }

        return ans;
    }
};