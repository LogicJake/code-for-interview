#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs)
    {
        vector<vector<string>> ans;
        int n = strs.size();
        unordered_map<string, vector<string>> maps;

        for (int i = 0; i < n; ++i) {
            string temp = strs[i];
            sort(temp.begin(), temp.end());
            maps[temp].push_back(strs[i]);
        }

        for (auto iter = maps.begin(); iter != maps.end(); ++iter) {
            ans.emplace_back(iter->second);
        }

        return ans;
    }
};