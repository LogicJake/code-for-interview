#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
    int findKth(vector<int> a, int n, int K)
    {
        priority_queue<int, vector<int>, greater<int>> min_heap;

        for (int i = 0; i < K; i++) {
            min_heap.push(a[i]);
        }

        for (int i = K; i < n; i++) {
            if (a[i] > min_heap.top()) {
                min_heap.pop();
                min_heap.push(a[i]);
            }
        }

        return min_heap.top();
    }
};