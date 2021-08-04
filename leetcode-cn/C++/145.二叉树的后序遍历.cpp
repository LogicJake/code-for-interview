/*
 * @lc app=leetcode.cn id=145 lang=cpp
 *
 * [145] 二叉树的后序遍历
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root)
    {
        stack<TreeNode*> st;
        vector<int> ans;
        TreeNode* prev = nullptr;

        while (root != nullptr || !st.empty()) {
            while (root != nullptr) {
                st.push(root);
                root = root->left;
            }

            root = st.top();
            st.pop();

            if (root->right == nullptr || root->right == prev) {
                ans.push_back(root->val);
                prev = root;
                root = nullptr;
            } else {
                st.push(root);
                root = root->right;
            }
        }

        return ans;
    }
};
// @lc code=end
