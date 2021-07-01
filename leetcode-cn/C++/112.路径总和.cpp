/*
 * @lc app=leetcode.cn id=112 lang=cpp
 *
 * [112] 路径总和
 */

// @lc code=start
// struct TreeNode
// {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode() : val(0), left(nullptr), right(nullptr) {}
//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
// };

class Solution
{
public:
    bool hasPathSum(TreeNode *root, int targetSum)
    {
        if (root == nullptr)
        {
            return false;
        }

        targetSum = targetSum - root->val;

        if (targetSum == 0 && !root->left && !root->right)
        {
            return true;
        }

        return hasPathSum(root->left, targetSum) || hasPathSum(root->right, targetSum);
    }
};
// @lc code=end
