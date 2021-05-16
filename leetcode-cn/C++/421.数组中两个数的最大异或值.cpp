/*
 * @lc app=leetcode.cn id=421 lang=cpp
 *
 * [421] 数组中两个数的最大异或值
 */

// @lc code=start
#include <vector>
using namespace std;

struct Trie {
    // 左子树指向表示 0 的子节点
    Trie* left = nullptr;
    // 右子树指向表示 1 的子节点
    Trie* right = nullptr;

    Trie() { }
};

class Solution {

private:
    // 字典树的根节点
    Trie* root = new Trie();
    // 最高位的二进制位编号为 30
    static const int HIGH_BIT = 30;

    void add(int num)
    {
        Trie* cur = root;
        for (int i = HIGH_BIT; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (bit == 1) {
                if (!cur->right) {
                    cur->right = new Trie();
                }
                cur = cur->right;
            } else {
                if (!cur->left) {
                    cur->left = new Trie();
                }
                cur = cur->left;
            }
        }
    }

    int check(int num)
    {
        Trie* cur = root;
        int ans = 0;
        for (int i = HIGH_BIT; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (bit == 1) {
                if (cur->left) {
                    ans = ans * 2 + 1;
                    cur = cur->left;
                } else {
                    ans = ans * 2;
                    cur = cur->right;
                }
            } else {
                if (cur->right) {
                    ans = ans * 2 + 1;
                    cur = cur->right;
                } else {
                    ans = ans * 2;
                    cur = cur->left;
                }
            }
        }
        return ans;
    }

public:
    int findMaximumXOR(vector<int>& nums)
    {
        int ans = 0;
        for (int i = 1; i < nums.size(); i++) {
            add(nums[i - 1]);
            int num = check(nums[i]);
            ans = max(ans, num);
        }
        return ans;
    }
};
// @lc code=end
