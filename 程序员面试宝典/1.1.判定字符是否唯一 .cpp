#include <string>

using namespace std;

class Solution {
public:
    bool isUnique(string astr)
    {
        int mask = 0;
        for (char c : astr) {
            if (mask & (1 << c - 'a')) {
                return false;
            }
            mask |= (1 << c - 'a');
        }

        return true;
    }
};