#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    char firstUniqChar(string s)
    {
        unordered_map<char, int> cnt;

        for (char c : s) {
            cnt[c] += 1;
        }

        for (char c : s) {
            if (cnt[c] == 1) {
                return c;
            }
        }

        return ' ';
    }
};