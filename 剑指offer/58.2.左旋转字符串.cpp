class Solution {
public:
    string reverseLeftWords(string s, int n)
    {
        string st1 = s.substr(0, n);
        string st2 = s.substr(n);

        return st2 + st1;
    }
};