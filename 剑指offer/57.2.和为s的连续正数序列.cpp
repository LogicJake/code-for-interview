#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> findContinuousSequence(int target)
    {
        int left = 1;
        int right = 1;
        int window = 0;

        vector<vector<int>> ans;

        while (left < target / 2) {
            if (window == target) {
                vector<int> tmp;

                for (int i = left; i < right; i++) {
                    tmp.push_back(i);
                }

                ans.push_back(tmp);

                window -= left;
                left++;
            } else if (window < target) {
                window += right;
                right++;
            } else {
                window -= left;
                left++;
            }
        }

        return ans;
    }
};