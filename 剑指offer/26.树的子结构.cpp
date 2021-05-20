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
    bool isSame(TreeNode* A, TreeNode* B)
    {
        if (!B) {
            return true;
        }

        if (!A) {
            return false;
        }

        if (A->val != B->val) {
            return false;
        }

        return isSame(A->left, B->left) && isSame(A->right, B->right);
    }

    bool isSubStructure(TreeNode* A, TreeNode* B)
    {
        bool ans = false;

        if (!A || !B) {
            return false;
        }

        if (A->val == B->val) {
            ans = isSame(A, B);
        }

        if (!ans) {
            ans = isSubStructure(A->left, B);
        }

        if (!ans) {
            ans = isSubStructure(A->right, B);
        }

        return ans;
    }
};