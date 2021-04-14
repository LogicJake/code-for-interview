#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
    /**
     * return a array which include all ans for op3
     * @param op int整型vector<vector<>> operator
     * @return int整型vector
     */
    stack<int> s;
    stack<int> ms;

    vector<int> getMinStack(vector<vector<int>>& op)
    {
        vector<int> ans;

        for (int i = 0; i < op.size(); i++) {
            if (op[i][0] == 1) {
                Push(op[i][1]);
            } else if (op[i][0] == 2) {
                Pop();
            } else {
                int num = getMin();
                ans.push_back(num);
            }
        }

        return ans;
    }

    void Push(int x)
    {
        s.push(x);
        if (ms.empty() || ms.top() >= x) {
            ms.push(x);
        }
    }

    void Pop()
    {
        if (!s.empty()) {
            if (s.top() == ms.top()) {
                ms.pop();
            }
            s.pop();
        }
    }

    int getMin()
    {
        return ms.top();
    }
};