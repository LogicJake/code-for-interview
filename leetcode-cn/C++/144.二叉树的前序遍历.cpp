/*
 * @lc app=leetcode.cn id=144 lang=cpp
 *
 * [144] 二叉树的前序遍历
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
#include <vector>
#include <stack>

using namespace std;

class Solution
{
public:
    vector<int> preorderTraversal(TreeNode *root)
    {
        stack<TreeNode *> st;
        vector<int> ans;

        while (root || !st.empty())
        {
            if (root)
            {
                ans.push_back(root->val);

                if (root->right)
                {
                    st.push(root->right);
                }
                root = root->left;
            }
            else
            {
                root = st.top();
                st.pop();
            }
        }

        return ans;
    }
};
// @lc code=end
