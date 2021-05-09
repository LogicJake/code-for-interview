/*
 * @lc app=leetcode.cn id=1482 lang=cpp
 *
 * [1482] 制作 m 束花所需的最少天数
 */

// @lc code=start
#include <algorithm>
#include <vector>

using namespace std;
class Solution {
public:
    bool help(vector<int>& bloomDay, int m, int k, int day)
    {
        int n = 0;
        int cnt = 0;

        for (int i = 0; i < bloomDay.size(); i++) {
            if (bloomDay[i] <= day) {
                cnt += 1;
                if (cnt == k) {
                    n += 1;
                    cnt = 0;
                }
            } else {
                cnt = 0;
            }
        }

        return n >= m;
    }

    int minDays(vector<int>& bloomDay, int m, int k)
    {
        if (m * k > bloomDay.size()) {
            return -1;
        }

        int left = *min_element(bloomDay.begin(), bloomDay.end());
        int right = *max_element(bloomDay.begin(), bloomDay.end()) + 1;

        while (left < right) {
            int day = (right - left) / 2 + left;
            if (help(bloomDay, m, k, day)) {
                right = day;
            } else {
                left = day + 1;
            }
        }

        return left;
    }
};
// @lc code=end
