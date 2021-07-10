#include <vector>
using namespace std;
class Solution {
public:
    vector<int> findSquare(vector<vector<int>>& matrix)
    {
        vector<int> ans;
        int size = 0;

        int n = matrix.size();

        if(n==0){
            return {};
        }

        vector<vector<int>> dpx(n+1, vector<int>(n+1,0));
        vector<vector<int>> dpy(n+1, vector<int>(n+1,0));

        for(int i = n-1; i >= 0; i--){
            for(int j = n-1; j >= 0; j--){
                if (matrix[i][j] == 0){
                    dpx[i][j] = dpx[i][j+1] + 1;
                    dpy[i][j] = dpy[i+1][j] + 1;
                }
            }
        }

        for(int i=0; i < n; i++){
            for(int j =0;j<n;j++){
                int width = min(dpx[i][j], dpy[i][j]);
                for(int c = width; c>size; c--){
                    if(dpx[i+c-1][j]>=c && dpy[i][j+c-1]>=c){
                        size = c;
                        ans = {i, j, size};
                        break;
                    }
                }
            }
        }


        return ans;
    }
};