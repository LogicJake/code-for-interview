class Solution {
public:
    TreeNode* ans;

    bool help(TreeNode* root, TreeNode* p, TreeNode* q)
    {
        if (root == nullptr) {
            return false;
        }

        bool left = help(root->left, p, q);
        bool right = help(root->right, p, q);

        if ((left && right) || ((root == p || root == q) && (left || right))) {
            ans = root;
        }

        return left || right || root == p || root == q;
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q)
    {
        help(root, p, q);
        return ans;
    }
};