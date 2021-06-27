class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k)
    {
        deque<int> q;
        int n = nums.size();

        if (n == 0 || k == 0) {
            return {};
        }

        for (int i = 0; i < k; i++) {
            while (!q.empty() && nums[q.back()] < nums[i]) {
                q.pop_back();
            }
            q.push_back(i);
        }

        vector<int> ans;
        ans.push_back(nums[q.front()]);

        for (int i = k; i < n; i++) {
            while (!q.empty() && nums[q.back()] < nums[i]) {
                q.pop_back();
            }
            q.push_back(i);
            if (i - k == q.front()) {
                q.pop_front();
            }
            ans.push_back(nums[q.front()]);
        }

        return ans;
    }
};