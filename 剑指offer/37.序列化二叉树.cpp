#include <deque>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x)
        : val(x)
        , left(NULL)
        , right(NULL)
    {
    }
};
class Codec {
public:
    // Encodes a tree to a single string.
    void serialize(TreeNode* root, string& ans)
    {
        if (root == nullptr) {
            ans += "null,";
        } else {
            ans = ans + to_string(root->val) + ",";
            serialize(root->left, ans);
            serialize(root->right, ans);
        }
    }

    string serialize(TreeNode* root)
    {
        string ans;
        serialize(root, ans);
        return ans;
    }

    vector<string> split(const string& str, const string& pattern)
    {
        vector<string> res;
        if (str == "")
            return res;
        //在字符串末尾也加入分隔符，方便截取最后一段
        string strs = str + pattern;
        size_t pos = strs.find(pattern);

        while (pos != strs.npos) {
            string temp = strs.substr(0, pos);
            res.push_back(temp);
            //去掉已分割的字符串,在剩下的字符串中进行分割
            strs = strs.substr(pos + 1, strs.size());
            pos = strs.find(pattern);
        }

        return res;
    }

    TreeNode* rdeserialize(vector<string>& strs)
    {
        if (strs[0] == "null") {
            strs.erase(strs.begin());
            return nullptr;
        }

        TreeNode* root = new TreeNode(stoi(strs[0]));
        strs.erase(strs.begin());
        root->left = rdeserialize(strs);
        root->right = rdeserialize(strs);

        return root;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data)
    {
        vector<string> strs = split(data, ",");
        TreeNode* root = rdeserialize(strs);
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));