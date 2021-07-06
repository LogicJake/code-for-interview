/*
 * @lc app=leetcode.cn id=1418 lang=cpp
 *
 * [1418] 点菜展示表
 */

// @lc code=start
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution
{
public:
    vector<vector<string>> displayTable(vector<vector<string>> &orders)
    {
        unordered_set<int> tabels_st;
        unordered_set<string> foods_st;
        unordered_map<int, unordered_map<string, int>> tabel_num;

        for (vector<string> order : orders)
        {
            int tabel = stoi(order[1]);
            string food = order[2];

            tabels_st.insert(tabel);
            foods_st.insert(food);

            tabel_num[tabel][food]++;
        }

        vector<int> tabels;
        vector<string> foods;

        for (string food : foods_st)
        {
            foods.push_back(food);
        }

        for (int tabel : tabels_st)
        {
            tabels.push_back(tabel);
        }

        sort(tabels.begin(), tabels.end());
        sort(foods.begin(), foods.end());

        vector<vector<string>> ans;
        vector<string> tmp = foods;
        tmp.insert(tmp.begin(), "Table");
        ans.push_back(tmp);

        for (int tabel : tabels)
        {
            vector<string> tmp = {to_string(tabel)};

            for (string food : foods)
            {
                int num = tabel_num[tabel][food];
                tmp.push_back(to_string(num));
            }

            ans.push_back(tmp);
        }

        return ans;
    }
};
// @lc code=end
