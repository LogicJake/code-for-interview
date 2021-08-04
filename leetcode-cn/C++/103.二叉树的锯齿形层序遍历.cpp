/*
 * @lc app=leetcode.cn id=103 lang=cpp
 *
 * [103] 二叉树的锯齿形层序遍历
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
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root)
    {
        vector<vector<int>> ans;

        if (root == nullptr) {
            return ans;
        }

        int diretion = 0;
        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int sz = q.size();
            vector<int> temp;

            for (int i = 0; i < sz; i++) {
                root = q.front();
                q.pop();

                temp.push_back(root->val);

                if (root->left) {
                    q.push(root->left);
                }

                if (root->right) {
                    q.push(root->right);
                }
            }
            if (diretion == 0) {
                ans.push_back(temp);
            } else {
                reverse(temp.begin(), temp.end());
                ans.push_back(temp);
            }

            diretion = (diretion + 1) % 2;
        }

        return ans;
    }
};
// @lc code=end
