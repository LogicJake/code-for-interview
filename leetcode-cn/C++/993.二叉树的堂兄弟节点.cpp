/*
 * @lc app=leetcode.cn id=993 lang=cpp
 *
 * [993] 二叉树的堂兄弟节点
 */

// @lc code=start
#include <queue>
using namespace std;

// struct TreeNode {
//     int val;
//     TreeNode* left;
//     TreeNode* right;
//     TreeNode()
//         : val(0)
//         , left(nullptr)
//         , right(nullptr)
//     {
//     }
//     TreeNode(int x)
//         : val(x)
//         , left(nullptr)
//         , right(nullptr)
//     {
//     }
//     TreeNode(int x, TreeNode* left, TreeNode* right)
//         : val(x)
//         , left(left)
//         , right(right)
//     {
//     }
// };

class Solution {
public:
    int x = 0;
    int y = 0;

    TreeNode* x_parent;
    TreeNode* y_parent;

    int x_depth;
    int y_depth;

    void dfs(TreeNode* root, TreeNode* parent, int depth)
    {
        if (!root) {
            return;
        }

        if (root->val == x) {
            x_parent = parent;
            x_depth = depth;
        }

        if (root->val == y) {
            y_parent = parent;
            y_depth = depth;
        }

        dfs(root->right, root, depth + 1);
        dfs(root->left, root, depth + 1);
    }

    bool isCousins(TreeNode* root, int x, int y)
    {
        this->x = x;
        this->y = y;

        dfs(root, nullptr, 0);

        return x_depth == y_depth && x_parent != y_parent;
    }
};
// @lc code=end
