#include <vector>

#include <unordered_set>

using namespace std;

class Solution {
public:
    int findRepeatNumber(vector<int>& nums)
    {
        unordered_set<int> mem;
        int ans = -1;

        for (int num : nums) {
            if (mem.count(num)) {
                ans = num;
                break;
            }
            mem.insert(num);
        }
        return ans;
    }
};