#include <vector>
using namespace std;

class Solution {
public:
    int MoreThanHalfNum_Solution(vector<int> numbers)
    {
        int ans = -1;
        int cnt = 0;

        for (int val : numbers) {
            if (cnt == 0) {
                ans = val;
            }

            if (val == ans) {
                cnt += 1;

            } else {
                cnt -= 1;
            }
        }

        cnt = 0;
        for (int val : numbers) {
            if (val == ans) {
                cnt += 1;
            }
        }
        if (cnt > numbers.size() / 2) {
            return ans;
        } else {
            return 0;
        }
    }
};