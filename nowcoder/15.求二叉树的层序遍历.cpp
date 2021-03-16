#include <queue>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

class Solution {
public:
    /**
     * 
     * @param root TreeNode类 
     * @return int整型vector<vector<>>
     */
    vector<vector<int>> levelOrder(TreeNode* root)
    {
        if (!root) {
            return {};
        }

        deque<TreeNode*> queue;
        queue.push_back(root);

        vector<vector<int>> ans;

        while (!queue.empty()) {
            vector<int> tmp;
            int cnt = queue.size();
            for (int i = 0; i < cnt; i++) {
                TreeNode* root = queue.front();
                queue.pop_front();
                tmp.push_back(root->val);
                if (root->left) {
                    queue.push_back(root->left);
                }
                if (root->right) {
                    queue.push_back(root->right);
                }
            }

            ans.push_back(tmp);
        }
        return ans;
    }
};