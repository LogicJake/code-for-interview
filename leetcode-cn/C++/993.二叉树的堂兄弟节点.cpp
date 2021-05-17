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

    void update(TreeNode* cur, TreeNode* parent, int depth)
    {
        if (cur->val == x) {
            x_depth = depth;
            x_found = true;
            x_parent = parent;
        }

        if (cur->val == y) {
            y_depth = depth;
            y_found = true;
            y_parent = parent;
        }
    }

    bool isCousins(TreeNode* root, int x, int y)
    {
        this->x = x;
        this->y = y;
        queue<pair<TreeNode*, int>> q;
        q.push({ root, 0 });
        update(root, nullptr, 0);

        while (!q.empty()) {
            auto [cur, depth] = q.front();
            q.pop();

            if (cur->left) {
                update(cur->left, cur, depth + 1);
                q.push({ cur->left, depth + 1 });
            }

            if (cur->right) {
                update(cur->right, cur, depth + 1);
                q.push({ cur->right, depth + 1 });
            }
        }

        return x_depth == y_depth && x_parent != y_parent;
    }
};
// @lc code=end
