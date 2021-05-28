#include <algorithm>
#include <set>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> ans;
    int n = 0;

    void help(vector<char> candiate, string temp, vector<bool> visited)
    {
        if (temp.size() == candiate.size()) {
            ans.push_back(temp);
            return;
        }

        set<char> visited_c;
        for (int i = 0; i < candiate.size(); i++) {
            if (visited[i] or visited_c.count(candiate[i])) {
                continue;
            }

            visited_c.insert(candiate[i]);
            visited[i] = true;
            help(candiate, temp + candiate[i], visited);
            visited[i] = false;
        }
    }

    vector<string> permutation(string s)
    {
        vector<char> c_list;
        vector<bool> visited(s.size(), false);
        string temp = "";

        for (char c : s) {
            c_list.push_back(c);
        }

        help(c_list, temp, visited);
        return ans;
    }
};