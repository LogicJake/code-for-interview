/*
 * @lc app=leetcode.cn id=116 lang=cpp
 *
 * [116] 填充每个节点的下一个右侧节点指针
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        queue<Node*> q;

        if(root == nullptr){
            return root;
        }

        q.push(root);

        while(!q.empty()){
            int sz = q.size();
            Node* pre = nullptr;
            for(int i = 0; i < sz; i++){
                Node* cur = q.front();
                q.pop();

                if(cur->left){
                    q.push(cur->left);
                }

                if(cur->right){
                    q.push(cur->right);
                }

                if (pre){
                    pre->next = cur;
                }
                pre = cur;
            }
        }

        return root;
        
    }
};
// @lc code=end

