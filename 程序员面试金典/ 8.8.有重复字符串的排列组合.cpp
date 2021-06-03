#include <algorithm>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string path = "";
    vector<string> ans;
    string S;

    void help(vector<int> visited)
    {
        if (path.length() == S.length()) {
            ans.push_back(path);
            return;
        }

        for (int i = 0; i < S.length(); i++) {
            if (visited[i] == 1) {
                continue;
            }

            if (i > 0 && visited[i - 1] == 0 && S[i] == S[i - 1]) {
                continue;
            }

            path.push_back(S[i]);
            visited[i] = 1;
            help(visited);
            visited[i] = 0;
            path.pop_back();
        }
    }

    vector<string> permutation(string S)
    {
        sort(S.begin(), S.end());
        this->S = S;
        vector<int> visited(S.length(), 0);
        help(visited);
        return ans;
    }
};