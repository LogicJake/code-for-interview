#include <string>
using namespace std;

class Solution {
public:
    bool oneEditAway(string first, string second)
    {
        int len1 = first.size();
        int len2 = second.size();

        if (abs(len1 - len2) > 1) {
            return false;
        }

        int i = 0;
        int j = 0;
        int cnt = 0;

        while (i < len1 && j < len2) {
            if (first[i] == second[j]) {
                i += 1;
                j += 1;
            } else {
                cnt += 1;
                if (cnt > 1) {
                    return false;
                }

                if (len1 == len2) {
                    i += 1;
                    j += 1;
                } else if (len1 < len2) {
                    j += 1;
                } else if (len1 > len2) {
                    i += 1;
                }
            }
        }
        return true;
    }
};