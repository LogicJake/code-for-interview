class Solution {
public:
    int add(int a, int b)
    {
        while (b != 0) {
            int sum_ = a ^ b;
            int carry = (unsigned)(a & b) << 1;

            a = sum_;
            b = carry;
        }
        return a;
    }
};