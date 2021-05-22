#include <iostream>
#include <limits.h>

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
    bool help(TreeNode* root, long minVal, long maxVal)
    {
        if (!root) {
            return true;
        }

        if (root->val <= minVal || root->val >= maxVal) {
            return false;
        }

        return help(root->left, minVal, root->val) && help(root->right, root->val, maxVal);
    }

    bool isValidBST(TreeNode* root)
    {
        return help(root, LONG_MIN, LONG_MAX);
    }
};