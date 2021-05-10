/*
 * @lc app=leetcode.cn id=872 lang=cpp
 *
 * [872] 叶子相似的树
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
    void dfs(TreeNode* root, vector<int>& seq)
    {
        if (!root) {
            return;
        }

        if (!root->left && !root->right) {
            seq.push_back(root->val);
        }

        dfs(root->left, seq);
        dfs(root->right, seq);
    }

    bool leafSimilar(TreeNode* root1, TreeNode* root2)
    {
        vector<int> seq1;
        dfs(root1, seq1);

        vector<int> seq2;
        dfs(root2, seq2);

        return seq1 == seq2;
    }
};
// @lc code=end
