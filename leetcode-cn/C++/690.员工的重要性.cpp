/*
 * @lc app=leetcode.cn id=690 lang=cpp
 *
 * [690] 员工的重要性
 */

// @lc code=start

// class Employee {
// public:
//     int id;
//     int importance;
//     vector<int> subordinates;
// };

#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    void help(unordered_map<int, Employee*> id_map, Employee* cur, int& ans)
    {
        ans += cur->importance;
        for (int id : cur->subordinates) {
            help(id_map, id_map[id], ans);
        }
    }

    int getImportance(vector<Employee*> employees, int id)
    {
        unordered_map<int, Employee*> id_map;
        int ans = 0;

        for (Employee* e : employees) {
            id_map[e->id] = e;
        }

        help(id_map, id_map[id], ans);

        return ans;
    }
};
// @lc code=end
