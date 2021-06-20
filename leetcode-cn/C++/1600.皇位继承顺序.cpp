/*
 * @lc app=leetcode.cn id=1600 lang=cpp
 *
 * [1600] 皇位继承顺序
 */

// @lc code=start
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class ThroneInheritance {
public:
    unordered_map<string, vector<string>> map;
    unordered_set<string> dead;
    string root;

    ThroneInheritance(string kingName)
    {
        root = kingName;
    }

    void birth(string parentName, string childName)
    {
        map[parentName].push_back(childName);
    }

    void death(string name)
    {
        dead.insert(name);
    }

    vector<string> getInheritanceOrder()
    {
        vector<string> ans;
        help(root, ans);
        return ans;
    }

    void help(string root, vector<string>& ans)
    {
        if (!dead.count(root)) {
            ans.push_back(root);
        }
        for (string child : map[root])
            help(child, ans);
    }
};

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance* obj = new ThroneInheritance(kingName);
 * obj->birth(parentName,childName);
 * obj->death(name);
 * vector<string> param_3 = obj->getInheritanceOrder();
 */
// @lc code=end
