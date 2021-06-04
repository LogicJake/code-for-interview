#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> path;
    vector<vector<int>> ans;
    vector<int> nums;

    int n = 0;

    void help(int index)
    {
        ans.push_back(path);

        for (int i = index; i < n; i++) {
            if (i > index && nums[i] == nums[i - 1]) {
                continue;
            }

            path.push_back(nums[i]);
            help(i + 1);
            path.pop_back();
        }
    }

    vector<vector<int>> subsets(vector<int>& nums)
    {
        sort(nums.begin(), nums.end());
        this->n = nums.size();
        this->nums = nums;
        help(0);
        return ans;
    }
};