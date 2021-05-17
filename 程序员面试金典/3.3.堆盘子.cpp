#include <stack>
#include <vector>
using namespace std;

class StackOfPlates {
public:
    vector<stack<int>> sts;
    int cap;

    StackOfPlates(int cap)
    {
        this->cap = cap;
    }

    void push(int val)
    {
        if (cap == 0) {
            return;
        }

        if (sts.empty() || sts.back().size() == cap) {
            sts.emplace_back(stack<int>());
        }
        sts.back().push(val);
    }

    int pop()
    {
        if (cap == 0 || sts.empty()) {
            return -1;
        }
        int res = sts.back().top();
        sts.back().pop();
        if (sts.back().empty()) {
            sts.pop_back();
        }
        return res;
    }

    int popAt(int index)
    {
        if (cap == 0 || index >= sts.size()) {
            return -1;
        }
        int res = sts[index].top();
        sts[index].pop();
        if (sts[index].empty()) {
            sts.erase(sts.begin() + index);
        }
        return res;
    }
};
