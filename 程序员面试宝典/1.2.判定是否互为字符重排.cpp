#include <algorithm>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool CheckPermutation(string s1, string s2)
    {
        unordered_map<char, int> mem1;
        unordered_map<char, int> mem2;

        for (char c : s1) {
            mem1[c] += 1;
        }

        for (char c : s2) {
            mem2[c] += 1;
            if (mem2[c] > mem1[c]) {
                return false;
            }
        }

        return mem1 == mem2;
    }
};