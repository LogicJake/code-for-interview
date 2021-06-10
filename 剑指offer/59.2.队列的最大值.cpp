#include <deque>
using namespace std;
class MaxQueue {
public:
    deque<int> que;
    deque<int> max_que;

    MaxQueue()
    {
        deque<int> que;
        this->que = que;

        deque<int> max_que;
        this->max_que = max_que;
    }

    int max_value()
    {
        if (not max_que.empty()) {
            return max_que.front();
        } else {
            return -1;
        }
    }

    void push_back(int value)
    {
        while (not max_que.empty() && max_que.back() < value) {
            max_que.pop_back();
        }
        max_que.push_back(value);
        que.push_back(value);
    }

    int pop_front()
    {
        if (que.empty()) {
            return -1;
        }
        int ans = que.front();
        if (ans == max_que.front()) {
            max_que.pop_front();
        }
        que.pop_front();
        return ans;
    }
};
