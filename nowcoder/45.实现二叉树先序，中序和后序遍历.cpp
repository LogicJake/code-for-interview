#include <vector>

using namespace std;

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

class Solution {
public:
    vector<int> preOrderRes;
    vector<int> inOrderRes;
    vector<int> postOrderRes;
    /**
     * 
     * @param root TreeNode类 the root of binary tree
     * @return int整型vector<vector<>>
     */

    void inOrder(TreeNode* root)
    {
        if (!root) {
            return;
        }

        inOrder(root->left);
        inOrderRes.push_back(root->val);
        inOrder(root->right);
    }

    void preOrder(TreeNode* root)
    {
        if (!root) {
            return;
        }

        preOrderRes.push_back(root->val);
        preOrder(root->left);
        preOrder(root->right);
    }

    void postOrder(TreeNode* root)
    {
        if (!root) {
            return;
        }

        postOrder(root->left);
        postOrder(root->right);
        postOrderRes.push_back(root->val);
    }

    vector<vector<int>> threeOrders(TreeNode* root)
    {
        vector<vector<int>> res;

        preOrder(root);
        res.push_back(preOrderRes);

        inOrder(root);
        res.push_back(inOrderRes);

        postOrder(root);
        res.push_back(postOrderRes);

        return res;
    }
};