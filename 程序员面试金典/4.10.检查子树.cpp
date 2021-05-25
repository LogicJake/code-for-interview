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
    bool checkSubTree(TreeNode* t1, TreeNode* t2)
    {
        if (!t2) {
            return true;
        }
        if (!t1) {
            return false;
        }
        if (t1->val != t2->val)
            return (checkSubTree(t1->left, t2) || checkSubTree(t1->right, t2));
        return (checkSubTree(t1->left, t2->left) && checkSubTree(t1->right, t2->right));
    }
};