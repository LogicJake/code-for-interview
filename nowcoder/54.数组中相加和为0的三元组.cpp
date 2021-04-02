#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& num)
    {
        int n = num.size();
        vector<vector<int>> ans;
        if (n < 3) {
            return ans;
        }

        sort(num.begin(), num.end());
        for (int i = 0; i < n - 2; i++) {
            if (num[i] > 0) {
                break;
            }
            if (i > 0 && num[i] == num[i - 1]) {
                continue;
            }

            int left = i + 1;
            int right = n - 1;

            while (left < right) {
                if (num[i] + num[left] + num[right] == 0) {
                    ans.push_back({ num[i], num[left], num[right] });

                    while (left < right && num[left] == num[left + 1]) {
                        left += 1;
                    }
                    while (left < right && num[right] == num[right - 1]) {
                        right -= 1;
                    }

                    left += 1;
                    right -= 1;
                } else if (num[i] + num[left] + num[right] < 0) {
                    left += 1;
                } else if (num[i] + num[left] + num[right] > 0) {
                    right -= 1;
                }
            }
        }
        return ans;
    }
};