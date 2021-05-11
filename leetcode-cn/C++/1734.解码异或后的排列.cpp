/*
 * @lc app=leetcode.cn id=1734 lang=cpp
 *
 * [1734] 解码异或后的排列
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> decode(vector<int>& encoded)
    {
        int n = encoded.size() + 1;
        int total = 0;

        for (int i = 1; i <= n; i++) {
            total ^= i;
        }

        // encoded[0] = perm[0] ^ perm[1]
        // encoded[1] = perm[1] ^ perm[2]
        // encoded[2] = perm[2] ^ perm[3]
        // encoded[3] = perm[3] ^ perm[4]
        int odd = 0;
        for (int i = 1; i < n - 1; i += 2) {
            odd ^= encoded[i];
        }

        vector<int> ans;
        ans.push_back(total ^ odd);

        for (int i = 0; i < n - 1; i++) {
            int last = ans.back();
            ans.push_back(encoded[i] ^ last);
        }
        return ans;
    }
};
// @lc code=end
