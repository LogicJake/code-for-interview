/*
 * @lc app=leetcode.cn id=149 lang=cpp
 *
 * [149] 直线上最多的点数
 */

// @lc code=start
class Solution {
public:
    int gcd(int x, int y)
    {
        if (y == 0) {
            return x;
        } else {
            return gcd(y, x % y);
        }
    }

    int maxPoints(vector<vector<int>>& points)
    {
        int ans = 1;

        for (int i = 0; i < points.size(); i++) {
            unordered_map<string, int> mem;

            vector<int> point1 = points[i];
            int x1 = point1[0];
            int y1 = point1[1];

            for (int j = i + 1; j < points.size(); j++) {
                vector<int> point2 = points[j];
                int x2 = point2[0];
                int y2 = point2[1];

                int mx = x2 - x1;
                int my = y2 - y1;

                if (my < 0) {
                    mx = -mx;
                    my = -my;
                }

                int k = gcd(mx, my);

                mx = mx / k;
                my = my / k;

                mem[to_string(mx) + "_" + to_string(my)]++;

                ans = max(ans, mem[to_string(mx) + "_" + to_string(my)] + 1);
            }
        }

        return ans;
    }
};
// @lc code=end
