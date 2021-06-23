#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        unordered_set<int> mem;

        for (int num : nums) {
            if (mem.count(target - num)) {
                return { target - num, num };
            } else {
                mem.insert(num);
            }
        }
        return {};
    }
};