#include <vector>
using namespace std;

class Solution {
public:
    bool help(const vector<int> postorder, int left, int right)
    {
        if (left > right) {
            return true;
        }

        int i = left;
        while (postorder[i] < postorder[right]) {
            i++;
        }

        int mid = i;

        while (postorder[i] > postorder[right]) {
            i++;
        }

        return i == right && help(postorder, left, mid - 1) && help(postorder, mid, right - 1);
    }

    bool verifyPostorder(vector<int>& postorder)
    {
        return help(postorder, 0, postorder.size() - 1);
    }
};