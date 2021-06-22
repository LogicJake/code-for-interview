#include <queue>
using namespace std;

class MedianFinder {
public:
    priority_queue<int, vector<int>, less<int>> maxHeap; // 大顶堆，存储较小的一半
    priority_queue<int, vector<int>, greater<int>> minHeap; // 小顶堆，存储较大的一半
    /** initialize your data structure here. */
    MedianFinder()
    {
    }

    void addNum(int num)
    {
        // 插入到较大的一边
        if (maxHeap.size() == minHeap.size()) {
            maxHeap.push(num);
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else {
            minHeap.push(num);
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double findMedian()
    {
        if (maxHeap.size() == minHeap.size()) {
            return (minHeap.top() + maxHeap.top()) / 2.0;
        } else {
            return minHeap.top() * 1.0;
        }
    }
};
