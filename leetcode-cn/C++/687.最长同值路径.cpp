/*
 * @lc app=leetcode.cn id=687 lang=cpp
 *
 * [687] 最长同值路径
 */

// @lc code=start
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode()
        : val(0)
        , left(nullptr)
        , right(nullptr)
    {
    }
    TreeNode(int x)
        : val(x)
        , left(nullptr)
        , right(nullptr)
    {
    }
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x)
        , left(left)
        , right(right)
    {
    }
};
class Solution {
public:
    int ans = 0;

    int maxLen(TreeNode* root)
    {
        if (!root) {
            return 0;
        }
        int leftRet = maxLen(root->left);
        int rightRet = maxLen(root->right);

        int left = 0;
        int right = 0;
        if (root->left != nullptr && root->left->val == root->val) {
            left = leftRet + 1;
        }
        if (root->right != nullptr && root->right->val == root->val) {
            right = rightRet + 1;
        }

        ans = max(ans, left + right);
        return max(left, right);
    }

    int longestUnivaluePath(TreeNode* root)
    {
        maxLen(root);
        return ans;
    }
};
// @lc code=end
