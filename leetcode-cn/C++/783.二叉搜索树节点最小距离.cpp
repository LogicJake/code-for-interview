/*
 * @lc app=leetcode.cn id=783 lang=cpp
 *
 * [783] 二叉搜索树节点最小距离
 */

// @lc code=start
#include <algorithm>
#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x)
        : val(x)
        , left(NULL)
        , right(NULL)
    {
    }
};

class Solution {
public:
    int pre = -1;
    int ans = INT32_MAX;

    void dfs(TreeNode* root)
    {
        if (root == NULL) {
            return;
        }

        dfs(root->left);

        if (pre != -1) {
            ans = min(ans, root->val - pre);
        }
        pre = root->val;

        dfs(root->right);
    }

    int minDiffInBST(TreeNode* root)
    {
        dfs(root);
        return ans;
    }
};
// @lc code=end
