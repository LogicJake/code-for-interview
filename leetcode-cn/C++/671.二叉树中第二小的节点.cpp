/*
 * @lc app=leetcode.cn id=671 lang=cpp
 *
 * [671] 二叉树中第二小的节点
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution
{
public:
    int ans = -1;
    int rootvalue = -1;

    void help(TreeNode *root)
    {
        if (root == nullptr)
        {
            return;
        }

        if (ans != -1 && root->val >= ans)
        {
            return;
        }

        if (root->val > rootvalue)
        {
            ans = root->val;
        }

        help(root->left);
        help(root->right);
    }

    int findSecondMinimumValue(TreeNode *root)
    {
        rootvalue = root->val;
        help(root);
        return ans;
    }
};
// @lc code=end
