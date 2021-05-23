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
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p)
    {
        TreeNode* pre = NULL;
        while (p != root) {
            if (p->val <= root->val) {
                pre = root;
                root = root->left;
            } else {
                root = root->right;
            }
        }

        if (p->right) {
            p = p->right;
            while (p->left) {
                p = p->left;
            }
            return p;
        } else {
            return pre;
        }
    }
};