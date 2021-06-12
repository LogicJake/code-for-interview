#include <vector>
using namespace std;

class Solution {
public:
    vector<int> constructArr(vector<int>& a)
    {
        vector<int> ans;
        int n = a.size();
        vector<int> num1(n, 1);
        vector<int> num2(n, 1);

        for (int i = 1; i < n; i++) {
            num1[i] = num1[i - 1] * a[i - 1];
            num2[i] = num2[i - 1] * a[n - i];
        }

        for (int i = 0; i < n; i++) {
            ans.push_back(num1[i] * num2[n - 1 - i]);
        }
        return ans;
    }
};