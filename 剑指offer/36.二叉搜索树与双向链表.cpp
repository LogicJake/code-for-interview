#include <iostream>
#include <vector>

using namespace std;

class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() { }

    Node(int _val)
    {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right)
    {
        val = _val;
        left = _left;
        right = _right;
    }
};

class Solution {
public:
    void help(Node* root, vector<Node*>& nodes)
    {
        if (!root) {
            return;
        }

        help(root->left, nodes);
        nodes.push_back(root);
        help(root->right, nodes);
    }

    Node* treeToDoublyList(Node* root)
    {
        vector<Node*> nodes;
        help(root, nodes);

        if (nodes.size() == 0) {
            return NULL;
        }

        Node* head = nodes[0];
        Node* pre = nodes[nodes.size() - 1];

        for (int i = 0; i < nodes.size(); i++) {
            Node* cur = nodes[i];

            Node* next = NULL;
            if (i == nodes.size() - 1) {
                next = head;
            } else {
                next = nodes[i + 1];
            }

            cur->right = next;
            cur->left = pre;

            pre = cur;
        }

        return head;
    }
};