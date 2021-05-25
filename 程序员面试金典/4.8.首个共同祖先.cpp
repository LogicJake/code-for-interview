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
    TreeNode* ans;

    bool dfs(TreeNode* root, TreeNode* p, TreeNode* q)
    {
        if (!root) {
            return false;
        }

        bool lson = dfs(root->left, p, q);
        bool rson = dfs(root->right, p, q);

        if (lson && rson || ((lson || rson) && (root == p || root == q))) {
            ans = root;
        }

        return lson || rson || root == p || root == q;
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q)
    {
        dfs(root, p, q);
        return ans;
    }
};