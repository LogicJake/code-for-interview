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

class Solution
{
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode *root)
    {
        int direction = 0;
        vector<vector<int>> ans;

        queue<TreeNode *> q;
        if (root == nullptr)
        {
            return {};
        }
        q.push(root);
        while (!q.empty())
        {
            int sz = q.size();
            vector<int> tmp;

            for (int i = 0; i < sz; i++)
            {
                auto root = q.front();
                q.pop();
                tmp.push_back(root->val);

                if (root->left)
                {
                    q.push(root->left);
                }

                if (root->right)
                {
                    q.push(root->right);
                }
            }

            if (direction == 0)
            {
                ans.push_back(tmp);
            }
            else
            {
                reverse(tmp.begin(), tmp.end());
                ans.push_back(tmp);
            }
            direction = (direction + 1) % 2;
        }

        return ans;
    }
};
// @lc code=end
