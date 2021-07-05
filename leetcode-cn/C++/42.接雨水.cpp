/*
 * @lc app=leetcode.cn id=42 lang=cpp
 *
 * [42] 接雨水
 */

// @lc code=start
#include <vector>
#include <stack>
using namespace std;

class Solution
{
public:
    int trap(vector<int> &height)
    {
        stack<int> st;
        int ans = 0;

        for (int i = 0; i < height.size(); i++)
        {
            while (!st.empty() && height[st.top()] < height[i])
            {
                int button = st.top();
                st.pop();

                if (st.empty())
                {
                    break;
                }

                int left = st.top();

                int w = i - left - 1;
                int h = min(height[i], height[left]) - height[button];

                ans += w * h;
            }

            st.push(i);
        }

        return ans;
    }
};
// @lc code=end
