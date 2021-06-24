#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string reverseWords(string s)
    {
        vector<string> words;
        string word = "";
        for (char c : s) {
            if (c == ' ') {
                if (word != "") {
                    words.push_back(word);
                    word = "";
                }
            } else {
                word.push_back(c);
            }
        }

        if (word != "") {
            words.push_back(word);
            word = "";
        }

        string ans = "";

        for (int i = words.size() - 1; i >= 0; i--) {
            ans += words[i];
            ans += " ";
        }

        ans.pop_back();

        return ans;
    }
};