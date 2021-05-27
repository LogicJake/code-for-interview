#include <algorithm>
#include <set>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> ans;
    bool find = false;
    vector<string> wordList;
    set<string> search;

    string endWord;

    void help(string word)
    {
        if (!count(wordList.begin(), wordList.end(), word)) {
            return;
        }

        if (count(search.begin(), search.end(), word)) {
            return;
        }

        if (word == endWord) {
            ans.push_back(endWord);
            find = true;
            return;
        }

        search.insert(word);
        for (int i = 0; i < word.size(); i++) {
            char tmp = word[i];

            for (char j = 'a'; j <= 'z'; j++) {
                word[i] = j;
                ans.push_back(word);
                help(word);
                ans.pop_back();
                if (find) {
                    break;
                }
            }

            if (find) {
                break;
            }

            word[i] = tmp;
        }
    }

    vector<string> findLadders(string beginWord, string endWord, vector<string>& wordList)
    {
        this->endWord = endWord;
        this->wordList = wordList;
        this->ans.push_back(beginWord);
        this->wordList.push_back(beginWord);
        help(beginWord);
        return ans;
    }
};