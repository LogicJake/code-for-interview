/*
 * @lc app=leetcode.cn id=897 lang=cpp
 *
 * [897] 递增顺序搜索树
 */

// @lc code=start
#include <vector>
using namespace std;

// struct TreeNode {
//     int val;
//     TreeNode* left;
//     TreeNode* right;
//     TreeNode()
//         : val(0)
//         , left(nullptr)
//         , right(nullptr)
//     {
//     }
//     TreeNode(int x)
//         : val(x)
//         , left(nullptr)
//         , right(nullptr)
//     {
//     }
//     TreeNode(int x, TreeNode* left, TreeNode* right)
//         : val(x)
//         , left(left)
//         , right(right)
//     {
//     }
// };

class Solution {
public:
    void help(TreeNode* root, vector<int>& ans)
    {
        if (root == nullptr) {
            return;
        }
        help(root->left, ans);
        ans.push_back(root->val);
        help(root->right, ans);
    }

    TreeNode* increasingBST(TreeNode* root)
    {
        vector<int> ans;
        help(root, ans);

        TreeNode* dummy = new TreeNode();
        TreeNode* cur = dummy;

        for (int val : ans) {
            cur->right = new TreeNode(val);
            cur = cur->right;
        }

        return dummy->right;
    }
};
// @lc code=end
