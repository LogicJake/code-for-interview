4/*
 * @lc app=leetcode.cn id=1160 lang=cpp
 *
 * [1160] 拼写单词
 */

// @lc code=start
class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        int ans = 0;
        
        unordered_map<char, int> mem;
        for(char c: chars){
            mem[c]++;
        }

        for(string word: words){
            unordered_map<char, int> tmp = mem;

            bool fine = true;
            for(char c: word){
                if(tmp[c] == 0){
                    fine = false;
                    break;
                }
                else{
                    tmp[c]--;
                }
            }

            if (fine)
                ans += word.size();
        }


        return ans;
    }
};
// @lc code=end

