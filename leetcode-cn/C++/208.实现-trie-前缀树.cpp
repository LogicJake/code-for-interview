/*
 * @lc app=leetcode.cn id=208 lang=cpp
 *
 * [208] 实现 Trie (前缀树)
 */

// @lc code=start
#include <memory.h>
#include <string>
using namespace std;

class Trie {
private:
    bool isEnd;
    Trie* next[26];

public:
    /** Initialize your data structure here. */
    Trie()
    {
        isEnd = false;
        memset(next, 0, sizeof(next));
    }

    /** Inserts a word into the trie. */
    void insert(string word)
    {
        Trie* cur = this;
        for (char ch : word) {
            if (cur->next[ch - 'a'] == NULL) {
                cur->next[ch - 'a'] = new Trie();
            }
            cur = cur->next[ch - 'a'];
        }
        cur->isEnd = true;
    }

    /** Returns if the word is in the trie. */
    bool search(string word)
    {
        Trie* cur = this;
        for (char ch : word) {
            if (cur->next[ch - 'a'] == NULL) {
                return false;
            }
            cur = cur->next[ch - 'a'];
        }
        return cur->isEnd;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix)
    {
        Trie* cur = this;
        for (char ch : prefix) {
            if (cur->next[ch - 'a'] == NULL) {
                return false;
            }
            cur = cur->next[ch - 'a'];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
// @lc code=end
