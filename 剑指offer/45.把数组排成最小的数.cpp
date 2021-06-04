#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    static bool compare(const string& s1, const string& s2)
    {
        string ab = s1 + s2;
        string ba = s2 + s1;
        return ab < ba; //升序排列。如改为ab > ba, 则为降序排列
    }

    string minNumber(vector<int>& nums)
    {
        vector<string> strs;
        for (int num : nums) {
            strs.push_back(to_string(num));
        }

        sort(strs.begin(), strs.end(), compare);

        string ans = "";
        for (string num : strs) {
            ans.append(num);
        }

        return ans;
    }
};