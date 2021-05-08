/*
 * @lc app=leetcode.cn id=1723 lang=cpp
 *
 * [1723] 完成所有工作的最短时间
 */

// @lc code=start
#include <algorithm>
#include <functional>
#include <numeric>
#include <vector>

using namespace std;

class Solution {
public:
    int minimumTimeRequired(vector<int>& jobs, int k)
    {
        sort(jobs.begin(), jobs.end(), greater<int>());
        int left = jobs[0];
        int right = accumulate(jobs.begin(), jobs.end(), 0);

        while (left < right) {
            int mid = (left + right) / 2;
            if (check(jobs, k, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    bool check(vector<int>& jobs, int k, int limit)
    {
        vector<int> workloads(k, 0);
        return dfs(jobs, workloads, 0, limit);
    }

    bool dfs(vector<int>& jobs, vector<int> workloads, int index, int limit)
    {
        if (index == jobs.size()) {
            return true;
        }

        for (int i = 0; i < workloads.size(); i++) {
            if (workloads[i] + jobs[index] <= limit) {
                workloads[i] = workloads[i] + jobs[index];

                if (dfs(jobs, workloads, index + 1, limit)) {
                    return true;
                }

                workloads[i] = workloads[i] - jobs[index];
            }

            if (workloads[i] == 0 || workloads[i] + jobs[index] == limit) {
                break;
            }
        }
        return false;
    }
};
// @lc code=end
