class Solution {
public:
    int ans = 0;
    int sumNums(int n)
    {
        n > 0 && sumNums(n - 1);
        ans += n;
        return ans;
    }
};