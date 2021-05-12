#include <unordered_map>
#include <vector>
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
    unordered_map<int, int> mem;

    TreeNode* build(vector<int>& preorder, vector<int>& inorder, int preorder_left, int preorder_right, int inorder_left, int inorder_right)
    {
        if (preorder_left > preorder_right) {
            return NULL;
        }

        int val = preorder[preorder_left];
        int inorder_root = mem[val];
        int left_len = inorder_root - inorder_left;

        TreeNode* root = new TreeNode(val);
        root->left = build(preorder, inorder, preorder_left + 1, preorder_left + left_len, inorder_left, inorder_root - 1);
        root->right = build(preorder, inorder, preorder_left + left_len + 1, preorder_right, inorder_root + 1, inorder_right);
        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder)
    {
        for (int i = 0; i < inorder.size(); i++) {
            mem[inorder[i]] = i;
        }

        return build(preorder, inorder, 0, preorder.size() - 1, 0, inorder.size() - 1);
    }
};