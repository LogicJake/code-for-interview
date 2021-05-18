#include <stack>
using namespace std;

class SortedStack {
public:
    stack<int> st;
    stack<int> st1;

    SortedStack()
    {
    }

    void push(int val)
    {
        while (!st.empty() && st.top() < val) {
            st1.push(st.top());
            st.pop();
        }
        st.push(val);

        while (!st1.empty()) {
            st.push(st1.top());
            st1.pop();
        }
    }

    void pop()
    {
        if (!st.empty()) {
            st.pop();
        }
    }

    int peek()
    {
        if (!st.empty()) {
            return st.top();
        }
        return -1;
    }

    bool isEmpty()
    {
        return st.empty();
    }
};
