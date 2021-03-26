#include <algorithm>
#include <string>

using namespace std;

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 计算两个数之和
     * @param s string字符串 表示第一个整数
     * @param t string字符串 表示第二个整数
     * @return string字符串
     */
    string solve(string s, string t)
    {
        string ans;

        int i = s.length() - 1;
        int j = t.length() - 1;

        int carry = 0;
        while (i >= 0 || j >= 0 || carry != 0) {
            int x = 0;
            if (i >= 0) {
                x = s[i] - '0';
            }

            int y = 0;
            if (j >= 0) {
                y = t[j] - '0';
            }

            int res = x + y + carry;
            ans.push_back('0' + res % 10);
            carry = res / 10;

            i -= 1;
            j -= 1;
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};