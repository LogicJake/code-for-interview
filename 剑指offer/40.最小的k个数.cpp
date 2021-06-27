#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k)
    {
        if (k == 0) {
            return {};
        }

        priority_queue<int, vector<int>> pq;

        for (int i = 0; i < k; i++) {
            pq.push(arr[i]);
        }

        for (int i = k; i < arr.size(); i++) {
            if (arr[i] < pq.top()) {
                pq.pop();
                pq.push(arr[i]);
            }
        }
        vector<int> ans;

        for (int i = 0; i < k; i++) {
            ans.push_back(pq.top());
            pq.pop();
        }

        return ans;
    }
};