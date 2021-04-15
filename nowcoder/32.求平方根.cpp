class Solution {
public:
    /**
     * 
     * @param x int整型 
     * @return int整型
     */
    int sqrt(int x)
    {
        int left = 0;
        int right = x + 1;

        if (x == 0) {
            return 0;
        }

        while (left < right) {
            int ans = left + (right - left) / 2;
            if (ans < x / ans) {
                left = ans + 1;
            } else if (ans > x / ans) {
                right = ans;
            } else {
                return ans;
            }
        }

        if (left > x / left) {
            return left - 1;
        }

        return left;
    }
};