class Solution {
public:
    bool isStraight(vector<int>& nums)
    {
        int num = 0;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                num += 1;
            } else {
                if (i > 0 && nums[i - 1] != 0) {
                    int diff = nums[i] - nums[i - 1] - 1;
                    if (diff < 0) {
                        return false;
                    }
                    num -= diff;
                    if (num < 0) {
                        return false;
                    }
                }
            }
        }

        return true;
    }
};