/*
 * @lc app=leetcode.cn id=981 lang=cpp
 *
 * [981] 基于时间的键值存储
 */

// @lc code=start
#include <unordered_map>
using namespace std;

class TimeMap {
public:
    unordered_map<string, vector<pair<int, string>>> mp;

    /** Initialize your data structure here. */
    TimeMap() {
    }
    
    void set(string key, string value, int timestamp) {
        mp[key].emplace_back(timestamp, value);
    }
    
    string get(string key, int timestamp) {
        auto &pairs = mp[key];

        int left = 0;
        int right = pairs.size();

        while(left < right){
            int mid = left + (right - left) / 2;

            if(pairs[mid].first > timestamp){
                right = mid;
            }
            else{
                left = mid + 1;
            }
        }

        if (left>0){
            return pairs[left-1].second;
        }
        return "";
    }   
};


/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
// @lc code=end

