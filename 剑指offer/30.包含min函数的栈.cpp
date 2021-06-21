#include <stack>
using namespace std;

class MinStack {
public:
    /** initialize your data structure here. */
    stack<int> st1;
    stack<int> st2;

    MinStack()
    {
    }

    void push(int x)
    {
        st1.push(x);

        if (st2.empty() || st2.top() >= x) {
            st2.push(x);
        }
    }

    void pop()
    {
        if (st1.empty()) {
            return;
        }

        int ans = st1.top();

        st1.pop();

        if (st2.top() == ans) {
            st2.pop();
        }
    }

    int top()
    {
        if (st1.empty()) {
            return -1;
        }

        return st1.top();
    }

    int min()
    {
        if (st2.empty()) {
            return -1;
        }

        return st2.top();
    }
};
