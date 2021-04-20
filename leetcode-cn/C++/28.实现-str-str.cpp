/*
 * @lc app=leetcode.cn id=28 lang=cpp
 *
 * [28] 实现 strStr()
 */

// @lc code=start
#include <string>
using namespace std;
class Solution {
public:
    void getNext(int* next, const string& s)
    {
        int j = -1;
        next[0] = j;
        for (int i = 1; i < s.size(); i++) {
            while (j >= 0 && s[i] != s[+1]) {
                j = next[j];
            }
            if (s[i] == s[j + 1]) {
                j++;
            }
            next[i] = j;
        }
    }

    int strStr(string haystack, string needle)
    {
        if (needle.size() == 0) {
            return 0;
        }
        int next[needle.size()];
        getNext(next, needle);
        int j = -1;
        for (int i = 0; i < haystack.size(); i++) {
            while (j >= 0 && haystack[i] != needle[j + 1]) {
                j = next[j];
            }
            if (haystack[i] == needle[j + 1]) {
                j++;
            }
            if (j == (needle.size() - 1)) {
                return (i - needle.size() + 1);
            }
        }
        return -1;
    }
};

// @lc code=end
