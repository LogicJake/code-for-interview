class Solution {
public:
    int help(TreeNode* root, int sum)
    {
        if (!root) {
            return 0;
        }
        sum -= root->val;
        int ret = 0;
        if (sum == 0) {
            ret = 1;
        }

        return ret + help(root->left, sum) + help(root->right, sum);
    }

    int pathSum(TreeNode* root, int sum)
    {
        if (!root) {
            return 0;
        }
        return help(root, sum) + pathSum(root->left, sum) + pathSum(root->right, sum);
    }
};