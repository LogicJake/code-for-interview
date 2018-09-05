#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int n, num = 0;
    cin >> n;
    if (n < 2)
        return 0;                    //小于2的数不合法
    for (int i = 2; i * i <= n; i++) //根号n复杂度
    {
        while (n % i == 0)
        {
            n = n / i;
            num++;
        }
    }
    if (n != 1)                     //当n为质数
        num++;
    cout << num;
    return 0;
}