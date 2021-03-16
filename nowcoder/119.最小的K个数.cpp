#include <queue>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> GetLeastNumbers_Solution(vector<int> input, int k)
    {
        int length = input.size();
        if (k == 0 || k > length) {
            vector<int> res;
            return res;
        }
        priority_queue<int, vector<int>> max_heap;

        for (const int val : input) {
            if (max_heap.size() < k) {
                max_heap.push(val);
            } else {
                if (val < max_heap.top()) {
                    max_heap.pop();
                    max_heap.push(val);
                }
            }
        }

        vector<int> ans;
        while (!max_heap.empty()) {
            ans.insert(ans.begin(), max_heap.top());
            max_heap.pop();
        }
        return ans;
    }
};