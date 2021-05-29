#include <bitset>
#include <limits.h>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findClosedNumbers(int num)
    {
        if (num == 1)
            return { 2, -1 };
        if (num == 0xffffffff)
            return { -1, -1 };

        bitset<32> small(num);
        bitset<32> big(num);
        // 找到比 num 小的最大的数
        // 从低位往高位，找到第一个10位置，然后把10转为01，1全部移到高位，0全部移到低位
        int s = -1;
        for (int i = 1; i < 32; i++) {
            if (small[i] == 1 && small[i - 1] == 0) {
                small.flip(i);
                small.flip(i - 1);

                // 1全部移到高位，0全部移到低位
                int left = 0;
                int right = i - 1;
                while (left < right) {
                    while (left < right && small[left] == 0) {
                        left++;
                    }

                    while (left < right && small[right] == 1) {
                        right--;
                    }

                    small.flip(left);
                    small.flip(right);
                }
                s = (int)small.to_ulong();
                break;
            }
        }

        int b = -1;
        for (int i = 1; i < 32; i++) {
            if (big[i] == 0 && big[i - 1] == 1) {
                big.flip(i);
                big.flip(i - 1);

                // 1全部移到低位，0全部移到高位
                int left = 0;
                int right = i - 1;
                while (left < right) {
                    while (left < right && big[left] == 1) {
                        left++;
                    }

                    while (left < right && big[right] == 0) {
                        right--;
                    }

                    big.flip(left);
                    big.flip(right);
                }

                if (big.to_ulong() <= INT32_MAX) {
                    b = (int)big.to_ulong();
                }
                break;
            }
        }

        return { b, s };
    }
};