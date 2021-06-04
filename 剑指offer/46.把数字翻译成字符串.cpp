#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int translateNum(int num)
    {
        string nums = to_string(num);
        int n = nums.length();

        vector<int> dp(n + 1, 0);
        int p = 1;
        int q = 1;

        for (int i = 2; i <= n; i++) {
            int r = q;
            if (nums.substr(i - 2, 2) >= "10" && nums.substr(i - 2, 2) <= "25") {
                r += p;
            }
            p = q;
            q = r;
        }

        return q;
    }
};