#include <vector>
using namespace std;

class Solution
{
public:
    int majorityElement(vector<int> &nums)
    {
        int ans = -1;
        int cnt = 0;

        for (int num : nums)
        {
            if (cnt == 0)
            {
                ans = num;
            }
            if (num == ans)
            {
                cnt += 1;
            }
            else
            {
                cnt -= 1;
            }
        }

        cnt = 0;
        for (int num : nums)
        {
            if (num == ans)
            {
                cnt++;
            }
        }

        if (cnt * 2 > nums.size())
        {
            return ans;
        }
        else
        {
            return -1;
        }
    }
};