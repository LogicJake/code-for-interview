#include <algorithm>
#include <deque>
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root)
    {
        if (!root) {
            return {};
        }

        deque<TreeNode*> queue;
        vector<vector<int>> ans;

        queue.push_back(root);
        int flag = 0;

        while (!queue.empty()) {
            vector<int> tmp;

            int len = queue.size();
            for (int i = 0; i < len; i++) {
                root = queue.front();
                queue.pop_front();

                if (root->left) {
                    queue.push_back(root->left);
                }
                if (root->right) {
                    queue.push_back(root->right);
                }

                tmp.push_back(root->val);
            }

            if (flag == 0) {
                ans.push_back(tmp);
            } else {
                reverse(tmp.begin(), tmp.end());
                ans.push_back(tmp);
            }

            flag = (flag + 1) % 2;
        }

        return ans;
    }
};