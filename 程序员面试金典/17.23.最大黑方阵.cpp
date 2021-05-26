#include <vector>
using namespace std;
class Solution {
public:
    vector<int> findSquare(vector<vector<int>>& matrix)
    {
        int m = matrix.size();
        int n = matrix[0].size();

        vector<vector<int>> dpx(m + 1, vector<int>(n + 1, 0));
        vector<vector<int>> dpy(m + 1, vector<int>(n + 1, 0));

        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (matrix[i][j] == 0) {
                    dpx[i][j] = dpx[i][j + 1] + 1;
                    dpy[i][j] = dpy[i + 1][j] + 1;
                }
            }
        }

        vector<int> ans;
        int width = 0;
        // 枚举左上角的点
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // 当前点构成的正方形的上边和左边的最短值
                int cur = min(dpx[i][j], dpy[i][j]);

                if (cur > width) {
                    // 现在只能保证上边和左边长度为k，需要检查下边和右边
                    // 检查下边就要检查 dpx[i+k-1][j]是否大于k
                    // 检查右边就要检查 dpy[i][j+k-1]是否大于k
                    for (int k = cur; k > width; k--) {
                        if (dpx[i + k - 1][j] >= k && dpy[i][j + k - 1] >= k) {
                            width = max(width, k);
                            ans = { i, j, width };
                            break;
                        }
                    }
                }
            }
        }

        return ans;
    }
};