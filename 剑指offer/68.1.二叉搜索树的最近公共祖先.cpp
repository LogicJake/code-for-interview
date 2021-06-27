class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q)
    {
        TreeNode* ans = root;

        while (true) {
            if (p->val < ans->val && q->val < ans->val) {
                ans = ans->left;
            } else if (p->val > ans->val && q->val > ans->val) {
                ans = ans->right;
            } else {
                break;
            }
        }

        return ans;
    }
};