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
    int ans = 0;
    int k = 0;

    void help(TreeNode* root)
    {
        if (root == NULL or k == 0) {
            return;
        }

        help(root->right);

        k -= 1;
        if (k == 0) {
            ans = root->val;
        }

        help(root->left);
    }

    int kthLargest(TreeNode* root, int k)
    {
        this->k = k;
        help(root);
        return ans;
    }
};