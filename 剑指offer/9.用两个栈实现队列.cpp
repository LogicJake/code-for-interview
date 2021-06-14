#include <stack>
using namespace std;

class CQueue {
public:
    stack<int> st1;
    stack<int> st2;

    CQueue()
    {
    }

    void appendTail(int value)
    {
        this->st1.push(value);
    }

    int deleteHead()
    {
        if (st1.empty()) {
            return -1;
        }

        while (!st1.empty()) {
            int value = this->st1.top();
            this->st1.pop();

            this->st2.push(value);
        }

        int ret = this->st2.top();
        this->st2.pop();

        while (!st2.empty()) {
            int value = this->st2.top();
            this->st2.pop();

            this->st1.push(value);
        }

        return ret;
    }
};

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue* obj = new CQueue();
 * obj->appendTail(value);
 * int param_2 = obj->deleteHead();
 */