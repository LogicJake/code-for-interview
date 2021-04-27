/*
 * @lc app=leetcode.cn id=1011 lang=cpp
 *
 * [1011] 在 D 天内送达包裹的能力
 */

// @lc code=start
#include <algorithm>
#include <numeric>

#include <vector>

using namespace std;

class Solution {
public:
    int shipWithinDays(vector<int>& weights, int D)
    {
        int left = *max_element(weights.begin(), weights.end());
        int right = accumulate(weights.begin(), weights.end(), 0);

        while (left < right) {
            int mid = (left + right) / 2;

            int need = 1;
            int cur = 0;

            for (int w : weights) {
                if (cur + w > mid) {
                    cur = 0;
                    need += 1;
                }

                cur += w;
            }

            if (need <= D) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
// @lc code=end
