#include <iostream>
using namespace std;

struct TreeNode
{
    char val;
    struct TreeNode *lchild, *rchild;
    TreeNode(char c) : val(c), lchild(NULL), rchild(NULL) {}
};
string str;
int i;

TreeNode *createTree()
{
    char c = str[i++];
    if (c == '#')
        return NULL;
    TreeNode *root = new TreeNode(c);
    root->lchild = createTree();
    root->rchild = createTree();
    return root;
}

void inOrderTraverse(TreeNode *root)
{
    if (root == NULL)
        return;
    inOrderTraverse(root->lchild);
    cout << root->val << " ";
    inOrderTraverse(root->rchild);
}

int main()
{
    cin >> str;
    i = 0;
    TreeNode *root = createTree();
    inOrderTraverse(root);
    return 0;
}
