#include <map>
#include <vector>

using namespace std;

class Solution {
public:
    /**
     * 
     * @param numbers int整型vector 
     * @param target int整型 
     * @return int整型vector
     */
    vector<int> twoSum(vector<int>& numbers, int target)
    {
        map<int, int> mem;
        vector<int> ans;

        for (int i = 0; i < numbers.size(); i++) {
            int num = numbers[i];

            map<int, int>::iterator it = mem.find(target - num);
            if (it != mem.end()) {
                ans.push_back(mem[target - num] + 1);
                ans.push_back(i + 1);
                break;
            }
            mem[num] = i;
        }

        return ans;
    }
};