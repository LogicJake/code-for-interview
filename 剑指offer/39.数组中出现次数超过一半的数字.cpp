#include <vector>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums)
    {
        int ans = 0;
        int vote = 0;

        for (int num : nums) {
            if (vote == 0) {
                ans = num;
            }

            if (num == ans) {
                vote++;
            } else {
                vote--;
            }
        }

        return ans;
    }
};